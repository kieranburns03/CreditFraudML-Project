from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pandas import read_csv
import joblib
def get_data():
    dataset = read_csv('creditcard.csv')
    print(dataset.head())
    X = dataset.drop('Class', axis = 1)
    Y = dataset['Class']
    X_data = X.values
    Y_data = Y.values

    seed = 7
    test_size = 0.33
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
    return X_train, y_train, X_test, y_test
def xg(X_train, y_train, X_test, y_test):
    # fit model no data
    model = XGBClassifier()
    model.fit(X_train, y_train)
    print(model)
    joblib.dump(model, 'Models/XGBoostModel.sav') # saves the model to the disk
    preds = [round(value) for value in model.predict(X_test)]
    print(str(round(accuracy_score(y_test, preds)*100, 5))+'% - Accuracy Score')
X_train, y_train, X_test, y_test= get_data()
xg(X_train, y_train, X_test, y_test)