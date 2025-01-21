# LangGraph RAG Application

This application uses LangGraph to implement a **retrieval-augmented generation (RAG)** pipeline. It retrieves relevant information from indexed documents and generates concise answers to user queries using a local LLM.

## Features

- Retrieval of relevant context from documents using a vector store.

- Streaming intermediate steps for real-time feedback.

- Customisable prompt templates for fine-tuned responses.

- Support for synchronous and asynchronous execution modes.

- Integration with a local LLM using LangChain's OpenAI-style API.

---

### Setting up LM Studio and Using Meta-Llama-3.1-8B-Instruct-GGUF

To integrate the **Meta-Llama-3.1-8B-Instruct-GGUF** model with this application, follow these steps to configure LM Studio.

---

#### Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **LM Studio**
- Adequate system resources (minimum 16GB RAM for the 8B model).

---

#### Steps to Set Up LM Studio

1. **Download LM Studio**  
   Visit the [official LM Studio GitHub repository](https://github.com/example-repo) and download the latest version for your operating system.

2. **Install LM Studio**  
   Follow the installation instructions specific to your operating system:
   - macOS/Linux: Use the `.dmg` or `.deb` file.
   - Windows: Use the `.exe` installer.

3. **Download the Model**  
   Use the LM Studio interface to download the **Meta-Llama-3.1-8B-Instruct-GGUF** model. Alternatively, you can import a local GGUF model file if available.

4. **Enable the API in LM Studio**  
   - Open LM Studio.
   - Navigate to **Settings > API**.
   - Enable the **API Server**.
   - Note the API URL and port (default: `http://localhost:8080`).

5. **Verify the Setup**  
   Confirm that LM Studio is running and the model is loaded. Use the following command in your terminal:

   ```bash
   lmstudio --list-models
   ```

6. **Update the setup_components.py file**
    Make sure the setup_components.py file is updated with the correct API key and URL to ensure smooth communication between your application and LM Studio

---

## Code Setup Instructions

Clone the Repository:

```bash

git clone <repository-url>
cd Langraph-RAG
```

Create a Virtual Environment:

```bash

python -m venv venv
```

Activate the Virtual Environment:

- On Windows:

  ```bash

  .\venv\Scripts\activate

  ```

- On macOS/Linux:

  ```bash

  source venv/bin/activate
  ```

Install Dependencies:

```bash

pip install -r requirements.txt
```

---

## Usage

Run the Application:
Start the app:

```bash

python rag_with_langgraph.py
```

Enter a question when prompted:

```plaintext

Enter your question: What is Task Decomposition?
```

View the streamed output of each step (retrieval and generation), followed by the final answer:

```plaintext

{'retrieve': {'context': [Document(...)]}}
----------------
{'generate': {'answer': 'Task decomposition is ...'}}
----------------
```

### Stream Tokens

To stream generated tokens:

```python

for message, metadata in graph.stream({"question": question}, stream_mode="messages"):
    print(message.content, end="|")
```

---

## Customising the Prompt

You can modify the prompt template in the script to tailor the response style to suit your needs. Below is an example of a custom prompt template:

```python
from langchain_core.prompts import PromptTemplate

template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know.
Keep the answer concise and end with: "Thanks for asking!"

{context}

Question: {question}

Helpful Answer:"""
custom_rag_prompt = PromptTemplate.from_template(template)
```

### Explanation

- **`template`**: This defines how the context and question are formatted into a prompt for the model.

- **`custom_rag_prompt`**: This is a `PromptTemplate` object created from the provided template string.

### How to Use

Replace the default prompt in your script with `custom_rag_prompt`. For example, in the `generate` function:

```python

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = custom_rag_prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

```

This ensures the model uses the custom prompt for generating answers.

---

## Clearing the Vector Store

If the vector store becomes populated with duplicate or unnecessary documents, you can clear it using a dedicated script. This ensures the store remains clean and avoids indexing the same documents multiple times.

### Using the Clearing Script

Create a script like `clear_vector_store.py` with the following content:

```python

from setup_components import vector_store

# Clear the vector store
if hasattr(vector_store, "documents"):
    vector_store.documents = []  # Clear the document list
    print("Vector store cleared.")
else:
    print("No documents to clear.")
```

Run the script whenever needed:

```bash

python clear_vector_store.py
```

### Future Improvements

In the future, the application will:

- Check if documents are already indexed before adding them to avoid duplicates.

- Support storing vector data in longer-term storage (e.g., FAISS or a database) for better persistence and scalability.

---

## File Structure

```plaintext
Langraph-RAG/
├── setup_components.py  # Sets up the vector store and local LLM
├── rag_with_langgraph.py # Main application logic
├── requirements.txt      # Dependencies
├── clear_vector_store.py # Script to clear the vector store
└── README.md             # Documentation
```

---

## Future Enhancements

- Add support for persistent storage of indexed documents.
- Extend compatibility with external LLMs or APIs.
- Incorporate a web or CLI interface for easier user interaction.
