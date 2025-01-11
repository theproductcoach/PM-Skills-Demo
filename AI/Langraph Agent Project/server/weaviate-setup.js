import weaviate from 'weaviate-ts-client'

async function setupSchema() {
  const client = weaviate.client({
    scheme: 'http',
    host: 'localhost:8080', // or your cloud endpoint
  });

  // Define the class schema
  const schemaConfig = {
    class: 'Document',
    properties: [
      {
        name: 'title',
        dataType: ['text'],
      },
      {
        name: 'content',
        dataType: ['text'],
      },
    ],
    vectorizer: 'text2vec-openai', // or another vectorizer if you have a module
  };

  try {
    // Create class
    await client.schema
      .classCreator()
      .withClass(schemaConfig)
      .do();
    console.log('Schema created!');
  } catch (err) {
    console.error('Error creating schema or it already exists:', err);
  }
}

setupSchema();
