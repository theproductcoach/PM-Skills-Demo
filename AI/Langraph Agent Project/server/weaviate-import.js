const weaviate = require('weaviate-ts-client');

async function importData() {
  const client = weaviate.client({
    scheme: 'http',
    host: 'localhost:8080',
  });

  // Example docs
  const docs = [
    {
      title: 'NDA_1',
      content: 'This is a short NDA between Company A and Company B...',
    },
    {
      title: 'NDA_2',
      content: 'This NDA states that any confidential info must be protected...',
    },
    {
      title: 'NDA Playbook',
      content: 'Our best practices for NDAs include ensuring confidentiality clauses...',
    },
  ];

  for (let doc of docs) {
    try {
      const result = await client.data
        .creator()
        .withClassName('Document')
        .withProperties(doc)
        .do();
      console.log('Imported:', result);
    } catch (err) {
      console.error('Error importing doc:', err);
    }
  }
}

importData();
