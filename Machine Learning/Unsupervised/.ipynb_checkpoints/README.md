# Unsupervised ML Implementation Example

## Introduction

This is an example to show how to implement an unsupervised ML implementation using python. During my time working as a Product Manager in numerous companies there has been a general lack of infrastructure to implement and support these types of ML solutions. This has led me to instead create this example to demonstrate my understanding and application of the concept.

## Data

The data that is being used is contained in the 'delaney-solubility-with-descriptors.csv' file, this is a table with 5 columns. The actual content of the data isn't extremely important, but for context it is from and the original paper this was used in is 

### Import the Data

Grab the csv or equivalent you will be using. To do this we will be using pandas.

### Clean the Data (Optional)

Plenty of things to consider here: spaces, special characters, empty rows, missing fields etc. In this example there wasn't any need to clean the data as it was prepared already.  

### Split the data into training/test sets

Generally for this you should be using 70-80% of the data for training and the remainder for testing, to do this I used train_test_split from sklearn.  

## Select an algorithm and build models

In this case we use Linear Regression and Random Forests

## Train the model

We simply feed the training values into the model through model.fit and that should be sufficient, the accuracy of the model will depend on the testing size.

## Evaluate Model Performance

In this case we show the correlation between Mean Squared Error and R2 for the training and testing sets for both models. We also generated a comparison between the two models' performance.

## Visualisations

Finally, we generated two visualisations, one for the Linear Regression, with a trendline added, and one for a single tree in the Random Forest.
