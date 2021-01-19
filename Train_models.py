
import os
def Train_model(mdl):
    module = __import__(mdl.replace('Model', ''))
    module.get_data()





models_list = [['1', 'DecisionTreeModel'], ['2', 'RFCModel'], ['3', 'XGBoostModel'], ['a', 'all']]

modes = input('1.DecisionTree\n2. Random Forest Classifier\n3. XGBoost\na. All Models\n[example: \'1,2\']..:').split(',')

if ''.join(modes)== 'a':
    for i in range(len(models_list)-1):
        print('--- Training   {}   ---'.format(models_list[i][1]))
        Train_model(models_list[i][1])
        print('Sucess! - (Models/{}.sav)\n---------\ \n'.format(models_list[i][1]))
else:
    for i in range(len(modes)):
        mdl = models_list[int(modes[i])-1][1]
        print('--- Training   {}   ---'.format(mdl))
        Train_model(mdl)
        print('Sucess! - (Models/{}.sav)\n---------\ \n'.format(models_list[i][1]))