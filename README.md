# CreditFraudML-Project
### By Kieran Burns

This is machine learning project developed in python to detect fraudulent credit card transactions.
It makes use of these models from the scikit library:
* XGBoost
* Decision Trees
* Random Forest Classifier

The dataset used is available here https://www.kaggle.com/mlg-ulb/creditcardfraud and contains anonymised data from two days, where there is 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the frauds account for just 0.172% of all transactions.

The program main.py will ask the user which models they want to train, the program will call the subprogram for training each model on a random selection of the dataset. Each trained model is saved to disk in a .sav file so that new predictions can be made without having to retrain each model. They will then have the option to make predictions on the dataset for each. The transactions that the program classes as suspicious are saved to a csv file for later reference.
!['o1'](Assets/o1.png)
!['p1'](Assets/p1.png)
!['r1'](Assets/r1.png)

## Challenges
The data used is highly unbalanced which makes training more difficult. This can be overcome by oversampling the fraudulent transactions.
Furthermore, columns V1 to V28 have gone through a PCA transformation to reduce their dimensionality in order to make it confidential. This has made visualisation of the data necessary to understand the correlation between Fraudulent and non-fraudulent cases. graphs created using the matplotlib library for python. 
!['V10'](Assets/V10.png)
!['V27'](Assets/V27.png)

## Evaluation

The program also gives the user the opton to create a graph of the tree when building the Random Forest Classifier Model which is saved as a .dot file and converted into a PNG. This could be used to adapt the model in the future if the fraudsters use other tactics to avoid detection by the RFC Model.
!['tree'](Assets/Tree1.png)
