# Langraph Agent Project

A proof-of-concept application that demonstrates:

- A **React (Vite)** frontend with a simple chat interface.
- A **Node.js (Express)** backend that handles `/api/chat` requests.
- A **Weaviate** vector database (running locally via Docker) to store and query documents (e.g., NDAs).

## Overview

1. **Frontend (React + Vite)**  
   - Located in the `chat-poc` folder (or whichever name you used).  
   - Displays a chat interface with Bootstrap styling for a modern look.  
   - Sends user’s messages to the backend endpoint (`/api/chat`) and displays responses.

2. **Backend (Node.js + Express)**  
   - Located in the `server` folder.  
   - Exposes `/api/chat` to receive chat messages from the frontend.  
   - Connects to Weaviate (via `weaviate-ts-client`) to find relevant documents based on the user’s query.

3. **Weaviate Vector Database**  
   - Runs in a Docker container on port `8080`.  
   - Stores documents with a simple `Document` schema (`title`, `content`).  
   - Provides semantic or keyword-based search to retrieve relevant docs.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (LTS recommended)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (if running Weaviate locally)
- [LM Studio](https://lmstudio.ai/) (Meta-Llama-3.1-8B-Instruct-GGUF)

### 1. Spin Up Weaviate with Docker

```bash
docker run -p 8080:8080 \
  --name weaviate \
  semitechnologies/weaviate:latest
```

> If you need a specific vectorizer (e.g. `text2vec-huggingface`), add environment variables like:
>
> ```
> -e ENABLE_MODULES=text2vec-huggingface
> ```
>
> or use `vectorizer: 'none'` plus `.withBm25()` for keyword search.

### 2. (Optional) Create Schema & Import Sample Docs

In the `server` folder, you may have scripts like:

- `weaviate-setup.js` – Creates the `Document` class.
- `weaviate-import.js` – Inserts some sample documents (e.g., NDAs).

Run them if you haven’t already:

```bash
cd server
node weaviate-setup.js
node weaviate-import.js
```

### 3. Start the Backend

Inside the `server` folder:

```bash
npm install
node index.js
```

You should see:

```
Server listening on http://localhost:3001
```

### 4. Start the Frontend

In another terminal, go to the React app folder (e.g., `chat-poc`):

```bash
cd chat-poc
npm install
npm run dev
```

Vite will print out a local dev URL, typically `http://localhost:5173`.

### 5. Test the Chat

- Open `http://localhost:5173` in your browser.
- Type a message in the chatbox.
- The app will call the backend (`http://localhost:3001/api/chat`), which queries Weaviate for relevant documents and returns the response.

## Project Structure

```
Langraph Agent Project
├─ server/
│  ├─ index.js           # Express server with /api/chat endpoint
│  ├─ weaviate-setup.js  # (Optional) Creates Document schema in Weaviate
│  ├─ weaviate-import.js # (Optional) Imports sample docs (NDAs, etc.)
│  └─ package.json
└─ chat-poc/ (React + Vite app)
   ├─ src/
   │  ├─ Chat.jsx
   │  └─ App.jsx
   ├─ index.html
   └─ package.json
```

## Future Enhancements

- **LangChain / Langraph** integration: Let an agent decide when to query Weaviate vs. finalize a response.
- **LLM Summarization**: Instead of returning raw document text, pass it to an LLM for summarization or Q&A.
- **Authentication**: Secure the endpoints if needed (e.g., for private NDA documents).
- **Deployment**: Containerize the entire stack or deploy the frontend separately (Vercel/Netlify) and the backend on a server (AWS, Heroku, etc.).

---

That’s it! This README should provide a clear picture of what’s in your project and how to get it running. Feel free to customize as you continue developing.
