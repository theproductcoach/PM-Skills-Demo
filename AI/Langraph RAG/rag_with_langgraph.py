from langchain import hub
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph
from IPython.display import Image, display
from setup_components import vector_store, llm  # Import vector store and LLM from your setup_components file

# Load the RAG prompt from LangChain hub
prompt = hub.pull("rlm/rag-prompt")

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
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

# Build the graph for the RAG pipeline
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

# Save the graph as an image
with open("graph_visualisation.png", "wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())
print("Graph visualisation saved as graph_visualisation.png")

# Test the application
result = graph.invoke({"question": "What is Task Decomposition?"})

# Print the results
print(f'Context: {result["context"]}\n\n')
print(f'Answer: {result["answer"]}')
