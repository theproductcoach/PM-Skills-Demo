const express = require('express')
const app = express()
const port = 3000

//routes

app.get('/', (req, res) => {
    res.send('Hello Node API')
})

app.listen(3000, ()=> {
    console.log('Node API app is running on port 3000')
})


/*
app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
*/