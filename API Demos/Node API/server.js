const express = require('express')
const mongoose = require('mongoose')
const app = express()

//routes

app.get('/', (req, res) => {
    res.send('Hello Node API Testing')
})



mongoose.connect('mongodb+srv://admin:12345678Admin@theproductcoachapi.nvkemdd.mongodb.net/Node-API?retryWrites=true&w=majority&appName=TheProductCoachAPI')
.then(() => {
    console.log('connected to MongoDB')
    app.listen(3000, ()=> {
        console.log('Node API app is running on port 3000')
    });
}).catch((error) => {
        console.error('MongoDB connection error:', error);
    });





//gQNiOALus0rGrqlv

//82.13.115.46
