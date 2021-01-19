from pandas import read_csv
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# for visualisation only
from sklearn.tree import export_graphviz
import pydot
import PIL.Image
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

def RFC(X_train, y_train, X_test, y_test):
    # random forest model creation
    rfc = RandomForestClassifier(verbose=True, n_jobs=-1)
    rfc.fit(X_train, y_train)
    joblib.dump(rfc, 'Models/RFCModel.sav')
    print('trained - \'Models/RFCModel.sav\'')
    return rfc, X_test
def visualise(rfc, X_test):
    # visualizing the random tree
    feature_list = list(X_test.columns)
    # Import tools needed for visualization

    # pulling out one tree from the forest
    tree = rfc.estimators_[5]
    export_graphviz(tree, out_file= "Analysis/RFC/tree.dot", feature_names = feature_list, rounded = True, precision = 1)
    # Use dot file to create a graph
    (graph,) = pydot.graph_from_dot_file("Analysis/RFC/tree.dot")
    # Write graph to a png file
    from subprocess import check_call
    check_call(['dot', '-Tpng', 'Analysis/RFC/tree.dot', '-o', 'Analysis/RFC/Tree.png'])
    img = PIL.Image.open('Analysis/RFC/Tree.png')
    img.show()
    print('Saving .dot file as \'Analysis/RFC/tree.dot\'\n Converting .dot graph to png (\'Analysis/RFC/Tree.png\')')
X_train, y_train, X_test, y_test= get_data()
rfc, X_test = RFC(X_train, y_train, X_test, y_test)

if input('Visualise the tree?[y/n]..: ') == 'y': visualise(rfc, X_test)
else:print('Complete')