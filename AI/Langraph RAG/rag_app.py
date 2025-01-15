from setup_components import llm, vector_store

import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

# Load and chunk contents of the blog
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
print("DEBUG: Loading documents...")
docs = loader.load()
print(f"DEBUG: {len(docs)} documents loaded.")

# Debug: Check if documents are loaded
print(f"Loaded {len(docs)} documents.")
for doc in docs[:3]:  # Print the first 3 documents as a sample
    print(f"Document Content: {doc.page_content[:200]}...\n")


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
print("DEBUG: Splitting documents...")
all_splits = text_splitter.split_documents(docs)
print(f"DEBUG: {len(all_splits)} document chunks created.")


# Debug: Check document chunks
print(f"Split documents into {len(all_splits)} chunks.")
for chunk in all_splits[:3]:  # Print the first 3 chunks as a sample
    print(f"Chunk Content: {chunk.page_content[:200]}...\n")


# Index chunks
print("DEBUG: Indexing documents...")
_ = vector_store.add_documents(documents=all_splits)
print("DEBUG: Documents indexed.")
print("Documents successfully indexed.")


# Debug: Check vector store content
test_query = "Task Decomposition"
retrieved_docs = vector_store.similarity_search(test_query, k=3)
print(f"Retrieved {len(retrieved_docs)} documents for the query: '{test_query}'")
for doc in retrieved_docs:
    print(f"Content: {doc.page_content[:200]}...\n")



# Define prompt for question-answering
prompt = hub.pull("rlm/rag-prompt")


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


# Define application steps
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}
    

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

response = graph.invoke({"question": "What is an AI Agent?"})
print(response["answer"])
