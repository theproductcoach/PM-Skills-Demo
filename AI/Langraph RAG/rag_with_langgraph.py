from setup_components import llm, vector_store

import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

# Original boilerplate prompt from https://python.langchain.com/docs/tutorials/rag/
# prompt = hub.pull("rlm/rag-prompt")

# Load and chunk contents of the blog
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)

print("Loading documents...")
docs = loader.load()
print(f"{len(docs)} documents loaded.")

# Debug: Check if documents are loaded
print(f"Loaded {len(docs)} documents.")
for doc in docs[:3]:  # Print the first 3 documents as a sample
    print(f"Document Content: {doc.page_content[:200]}...\n")


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
print("Splitting documents...")
all_splits = text_splitter.split_documents(docs)
print(f"{len(all_splits)} document chunks created.")


# Index chunks
print("Indexing documents...")
_ = vector_store.add_documents(documents=all_splits)
print("Documents indexed.")
print("Documents successfully indexed.")


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
    print("state",state)
    retrieved_docs = vector_store.similarity_search(state["question"])
    # Debugging: Print the retrieved document content
    print("\nRetrieved Contexts:")
    for doc in retrieved_docs:
        print(f"- {doc.page_content}\n")
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
with open("graph_visualisation.png", "wb") as f:
     f.write(graph.get_graph().draw_mermaid_png())
print("Graph visualisation saved as graph_visualisation.png")


# Ask the question dynamically
question = input("Enter your question: ")


# Stream intermediate steps
print("\nStreaming steps...\n")
for step in graph.stream({"question": question}, stream_mode="updates"):
    if 'retrieve' in step:
        print("\nRetrieved Contexts in 'retrieve' Step:")
        for doc in step['retrieve']['context']:
            print(f"- {doc.page_content}\n")
    print(f"{step}\n\n----------------\n")


# Print the final context and answer
result = graph.invoke({"question": question})
print(f'\nFinal Context: {result["context"]}\n\n')
print(f'Final Answer: {result["answer"]}')
