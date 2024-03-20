# Supervised ML Implementation Example

## Introduction

This is an example to show how to implement a supervised ML implementation using python. During my time working as a Product Manager in numerous companies there has been a general lack of infrastructure to implement and support these types of ML solutions. This has led me to instead create this example to demonstrate my understanding and application of the concept.

## Data

The data that is being used is contained in the 'music.csv' file, this is a table with 3 columns. This content is not real but shows the music preferences for men and women of different ages.

### Import the Data

Grab the csv or equivalent you will be using. To do this we will be using pandas.

### Clean the Data (Optional)

Plenty of things to consider here: spaces, special characters, empty rows, missing fields etc. In this example there wasn't any need to clean the data as it was prepared already.  

### Split the Data Into Training and Test Sets

Generally for this you should be using 70-80% of the data for training and the remainder for testing, to do this I used train_test_split from sklearn.  

## Select an algorithm and build models

In this case we use a Decision Tree Classifier

## Train the model

We simply feed the training values into the model through model.fit and that should be sufficient, the accuracy of the model will depend on the testing size (we used 20% in this case).

## Export the model

We export the model using joblib.dump, so that we can return to the model and use it without having to retrain it.

## Import the model

We import the model using joblib.load, so that we can return to the model and use it without having to retrain it.

## Visualisations

Finally, we generated a visualisation for the decision tree, exporting it as 'Music_Recommender.dot'
