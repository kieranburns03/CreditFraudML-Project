# CreditFraudML-Project
### By Kieran Burns

This is machine learning project developed in python to detect fraudulent credit card transactions.
It makes use of these models from the scikit library:
* XGBoost
* Decision Trees
* Random Forest Classifier

The dataset used is available here https://www.kaggle.com/mlg-ulb/creditcardfraud and contains anonymised data from two days, where there is 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the frauds account for just 0.172% of all transactions.

The program main.py will ask the user which models they want to train, each trained model is saved to disk so that new predictions can be made without having to retrain each model. They will then have the option to make predictions on the dataset for each model. The transactions that the program classes as suspicious are saved to a csv file for later reference.
!['train1'](Assets/o1.png)
!['p1'](Assets/p1.png)
!['r1'](Assets/r1.png)



!['V10'](Assets/V10.png)
!['V27'](Assets/V27.png)
