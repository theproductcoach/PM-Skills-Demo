# Supervised ML Implementation Example

## Introduction

This is an example to show how to implement a simple supervised ML implementation using python. The model developed will learn and predict the kinds of music people will like, then creating and utilising 'recommendation algorithm'. During my time working as a Product Manager in numerous companies there has been a general lack of infrastructure to implement and support these types of ML solutions. This has led me to instead create this example to demonstrate my understanding and application of the concept.

## Data

The data that is being used is contained in the 'music.csv' file, this is a very simple table with 3 columns: age, gender, and genre. This is the data that will be used to create our solution and is reprensentative of known preferences of our customers on an ecommerce website selling music.

## Cell 1  

Here is a description of what is happening in Cell 1:

### Import the Data

Grab the csv or equivalent you will be using. To do this we will be using pandas.

### Clean the Data (Optional)

Plenty of things to consider here: spaces, special characters, empty rows, missing fields etc. In this example there wasn't any need to clean the data as it was prepared already.  

### Split the data into training/test sets

Generally for this you should be using 70-80% of the data for training and the remainder for testing, to do this I used train_test_split from sklearn.

### Select an algorithm and build a model

In this case we're using a decision tree classifier

### Train the model

We simply feed the training values into the model through model.fit and that should be sufficient, the accuracy of the model will depend on the testing size.

### Make predictions with the model

I used the test values to generate predictions and then scored those predictions using accuracy_score.

### Evaluate Algorithm and Improve Accuracy

In this case the predictions were between 0.5 and 1.0 for accuracy, depending on the dataset used to train, however on re-reunning the predictions you can see that it trends towards higher accuracy.

## Cell 2

In Cell 2 we want to export the model to save and use for later without having to re-write all the code. So we have imported joblib, and saved the model as 'Music-Recommender.joblib' using joblib.dump.

## Cell 3

In Cell 3 we want to import the model to load and use. So we have imported joblib, and loaded the model using joblib.load. We can then easily pass predictions to the model and show that it's still working as intended.

## Cell 4

In Cell 4 we want to show a visualised breakdown of what the model is doing through it's decision tree. In this case we are importing the 'tree' from sklean and then expoorting the model as a .dot file. You can see an image representation of the tree [here](./Decision%20tree%20image.jpg). You can also view the .dot graph using VSCode extensions such as [this](https://marketplace.visualstudio.com/items?itemName=tintinweb.graphviz-interactive-preview) one.
