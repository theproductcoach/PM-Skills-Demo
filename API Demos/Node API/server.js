const express = require('express')
const mongoose = require('mongoose')
const Product = require('./models/productModel')
const app = express()
require('dotenv').config()


app.use(express.json())

//routes

app.get('/', (req, res) => {
    res.send('Hello Node API Testing')
})



//Get all products
app.get('/products', async(req, res) => {
    try {
        const product = await Product.find({})
        res.status(200).json(product);
    } catch (error) {
        res.status(500).json({message: error.message})
    }
})

//Get a single product
app.get('/products/:id', async(req, res) => {
    try {
        const {id} = req.params;
        const product = await Product.findById(id);
        res.status(200).json(product);
    } catch (error) {
        res.status(500).json({message: error.message})
    }
})

//Push Products
app.post('/products', async(req, res) => {
    try {
        const product = await Product.create(req.body)
        res.status(200).json(product);
    } catch (error) {
        console.log(error.message);
        res.status(500).json({message: error.message})
    }
})

//Update a product
app.put('/products/:id', async(req, res) => {
    try {
        const {id} = req.params;
        const product = await Product.findByIdAndUpdate(id, req.body);
        if(!product) {
            return res.status(404).json({message: `cannot find any product with ID ${id}`})
            //if we can't find it in the DB
        }
        const updatedProduct = await Product.findById(id);
        res.status(200).json(updatedProduct);
    } catch (error) {
        res.status(500).json({message: error.message})
    }
})

//Delete a product
app.delete('/products/:id', async(req, res) => {
    try {
        const {id} = req.params;
        const product = await Product.findByIdAndDelete(id);
        if(!product) {
            return res.status(404).json({message: `cannot find any product with ID ${id}`})
            //if we can't find it in the DB
        }
        res.status(200).json(product);
    } catch (error) {
        res.status(500).json({message: error.message})
    }
})

mongoose.connect(`mongodb+srv://admin:${process.env.MONGODB_PASSWORD}@theproductcoachapi.nvkemdd.mongodb.net/Node-API?retryWrites=true&w=majority&appName=TheProductCoachAPI`)
.then(() => {
    console.log('connected to MongoDB')
    app.listen(3000, ()=> {
        console.log('Node API app is running on port 3000')
    });
}).catch((error) => {
        console.error('MongoDB connection error:', error);
    });


//app.post('/product', (req, res) => {
//    console.log(req.body)
//    res.send(req.body)