from langchain_core.prompts import PromptTemplate
from langchain import hub
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph
from IPython.display import Image, display
from setup_components import vector_store, llm  # Import vector store and LLM from your setup_components file

# Original boilerplate prompt from https://python.langchain.com/docs/tutorials/rag/
# prompt = hub.pull("rlm/rag-prompt")

# Define the custom prompt
template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as concise as possible.
Always say "thanks for asking!" at the end of the answer.

{context}

Question: {question}

Helpful Answer:"""
custom_rag_prompt = PromptTemplate.from_template(template)

# Define the application state
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

# Define the retrieval step
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

# Define the generation step
def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    # Use the custom prompt instead of `prompt`
    messages = custom_rag_prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


# Build the graph for the RAG pipeline
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

# OPTIONAL Save the graph as an image
# with open("graph_visualisation.png", "wb") as f:
#     f.write(graph.get_graph().draw_mermaid_png())
# print("Graph visualisation saved as graph_visualisation.png")

# Test the application
# result = graph.invoke({"question": "What is an AI Agent?"})

# Test synchronous invocation
# result = graph.invoke({"question": "What is Task Decomposition?"})

# Define the question dynamically
question = input("Enter your question: ")

# Stream intermediate steps
print("\nStreaming steps...\n")
for step in graph.stream({"question": question}, stream_mode="updates"):
    print(f"{step}\n\n----------------\n")


# Print the retrieved context and answer
# print(f'Context: {result["context"]}\n\n')
# print(f'Answer: {result["answer"]}')

# Print the final context and answer
result = graph.invoke({"question": question})
print(f'\nFinal Context: {result["context"]}\n\n')
print(f'Final Answer: {result["answer"]}')
