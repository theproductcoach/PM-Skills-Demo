import weaviate from 'weaviate-ts-client';
import express from 'express';
import cors from 'cors';

const app = express();
const PORT = 3001;

app.use(express.json());
app.use(cors());

// Initialize the Weaviate client
const weaviateClient = weaviate.client({
  scheme: 'http',
  host: 'localhost:8001', // or your cloud endpoint
});

// Basic test route
app.get('/', (req, res) => {
  res.send('Hello from the backend!');
});

app.post('/api/chat', async (req, res) => {
  const { message } = req.body;

  try {
    // 1) Query Weaviate with nearText using the user's message
    const result = await weaviateClient.graphql
      .get()
      .withClassName('Document') // The class we created
      .withFields(['title', 'content'])
      .withNearText({ concepts: [message], distance: 0.7 })
      .withLimit(3) // Return top 3
      .do();

    // 2) Extract the results
    const docs = result.data.Get.Document || [];

    // 3) Create a response string or object
    let answer = '';
    if (docs.length === 0) {
      answer = `No documents found for: ${message}`;
    } else {
      answer = 'Top matching documents:\n\n';
      docs.forEach((doc, i) => {
        answer += `(${i + 1}) Title: ${doc.title}\nContent: ${doc.content}\n\n`;
      });
    }

    // 4) Return that as the "assistant" answer
    res.json({ answer });
  } catch (error) {
    console.error('Error querying Weaviate:', error);
    res.status(500).json({
      answer: 'Sorry, there was an error fetching results from Weaviate.',
    });
  }
});

app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});


