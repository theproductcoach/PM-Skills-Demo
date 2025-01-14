from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if you are using one)
load_dotenv()

# Retrieve and print the variables
tracing = os.getenv("LANGSMITH_TRACING")
api_key = os.getenv("LANGSMITH_API_KEY")

print(f"Tracing enabled: {tracing}")
print(f"API Key: {api_key}")
