
# loads save file and makes predictions without pre-training use 'main.py' to produce save file

from pandas import read_csv
from sklearn.metrics import accuracy_score
import joblib
import numpy
from pandas import DataFrame
import csv
dataset = read_csv('creditcard.csv')
X_test = dataset.drop('Class', axis = 1)
Y_test = dataset['Class']


def load_model(mdl, X_test, actual):
    saved_model = joblib.load('Models/{}.sav'.format(mdl))
    print('{} Transactions loaded from test set (\'Class\' Attribute has been omitted!)'.format(len(actual)))
    y_hats = saved_model.predict(X_test)
    print(accuracy_score(y_hats, actual))
############
    preds = list(y_hats)
    print(len(preds))
    X_test1 = X_test
    X_test = numpy.array(X_test)
    test_data_list = X_test.tolist()
    #print(test_data_list)
    s_count = 0
    writer = csv.writer(open('Analysis/Detected_{}.csv'.format(mdl), 'w'), delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13',
                            'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26',
                            'V27', 'V28', 'Amount'])
    #writer = csv.writer(open('Analysis/Detected_{}.csv'.format(mdl), 'wb'), delimiter=',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    for i in range(len(preds)):
        if preds[i] == 1:
            print('--------Suspicious--------')
            print(test_data_list[i])
            df = DataFrame([test_data_list[i]])
            df.to_csv('Analysis/Detected_{}.csv'.format(mdl), mode='a', index=False, header=False)
            s_count +=1
    print(str(s_count) + ' Suspicious Transactions found in test set')
    ys = Y_test.tolist()
    f_set = 0
    for item in range(len(ys)):
        if ys[item] == 1:
            f_set +=1
    print(str(f_set) + ' Actual Fraud in Test set')
###########


    #with open('Detected_{}.csv', 'w') as file: file.write(detected)
models_list = [['1', 'DecisionTreeModel'], ['2', 'RFCModel'], ['3', 'XGBoostModel'], ['a', 'all']]

modes = input('Predict----\n1.DecisionTree\n2. Random Forest Classifier\n3. XGBoost\na. All Models\n[example: \'1,2\']..:').split(',')
if ''.join(modes)== 'a':
    for i in range(len(models_list)-1):
        print('--- Running   {}   ---'.format(models_list[i][1]))
        load_model(models_list[i][1], X_test, Y_test)
        print('---------\ \n')
else:
    for i in range(len(modes)):
        mdl = models_list[int(modes[i])-1][1]
        print('--- Running   {}   ---'.format(mdl))
        load_model(mdl, X_test, Y_test)
        print('---------\ \n')
print('results saved to disk (CreditFraudML/Analysis/Detected_[Model name].csv)')