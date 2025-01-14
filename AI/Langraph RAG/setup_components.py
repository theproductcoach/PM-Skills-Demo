import os
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

# Set up the LM Studio chat model (OpenAI-style API)
# Replace "your-api-key" with a placeholder or actual API key if required
os.environ["OPENAI_API_KEY"] = "lm-studio"  # Required by LangChain, even if LM Studio doesn't enforce it
os.environ["OPENAI_API_BASE"] = "http://localhost:8000/v1"  # URL for LM Studio's OpenAI-style API

llm = ChatOpenAI(model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF")  # Replace with the model name from your LM Studio setup

# Set up the Hugging Face embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Set up the in-memory vector store
vector_store = InMemoryVectorStore(embeddings)

print("Components set up successfully!")

# Test the components
# response = llm("What is the capital of France?")
# print(f"LLM Response: {response}")
