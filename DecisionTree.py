 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from pandas import read_csv
import joblib
from sklearn.model_selection import train_test_split
def get_data():
    dataset = read_csv('creditcard.csv')
    print(dataset.head())
    X = dataset.drop('Class', axis = 1)
    Y = dataset['Class']
    X_data = X.values
    Y_data = Y.values
    X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, train_size=0.8)
    model = Decision_tree(X_test, X_train, Y_train)
    return X_test, Y_test, model
def Decision_tree(X_test, X_train, Y_train):
    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    # save the model to disk
    filename = 'Models/DecisionTreeModel.sav'
    joblib.dump(model, filename)
    return model
def predict(X_test, Y_test, model):
    y_hats = model.predict(X_test)
    preds = list(y_hats)
    test_data_list = X_test.tolist()
    s_count = 0
    for i in range(len(preds)):
        if preds[i] == 1:
            print('--------Suspicious--------')
            print(test_data_list[i])
            s_count = s_count + 1
    print(str(s_count) + ' Suspicious Transactions found in test set')
    ys = Y_test.tolist()
    f_set = 0
    for item in range(len(ys)):
        if ys[item] == 1:
            f_set = f_set +1
    print(str(f_set)+' Actual Fraud in Test set')
    print(str(accuracy_score(y_hats, Y_test)*100)+'% accurate.')
'''Disable for use by Train_models.py without interruption
mode = input('1 - Train model only\n2 - Train & Test\n..:')
if mode == '1':get_data()
elif mode == '2':
    X_test, Y_test, model = get_data()
    predict(X_test, Y_test, model)'''
