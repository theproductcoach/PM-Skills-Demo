// weaviate-setup.js
import weaviate from 'weaviate-ts-client';  // or require('weaviate-ts-client').default

async function setupSchema() {
  const client = weaviate.client({
    scheme: 'http',
    host: 'localhost:8001',
  });

  const classObj = {
    class: 'Document',
    description: 'A class to store documents with text embeddings.',
    vectorizer: 'text2vec-huggingface', // <--- Key part
    properties: [
      { name: 'title', dataType: ['text'] },
      { name: 'content', dataType: ['text'] },
    ],
  };

  try {
    await client.schema.classCreator().withClass(classObj).do();
    console.log('Created huggingface schema!');
  } catch (err) {
    console.error('Error creating schema:', err);
  }
}

setupSchema();
