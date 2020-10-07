import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.svm import SVC
from csv import reader
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVR
'''
# Load a CSV file
def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset'''

def trainModel():

    #chargement des données
    
    name="TEST_dataset.csv"
    df = pd.read_csv(name)
    print(df.head())
    #selection de la première colonne de notre dataset et redimensionnement
    X = df.iloc[1:len(df),0]
    X=X.values.reshape(len(X),1)
    print(len(df))
    #selection de deuxième colonnes de notre dataset et redimensionnement
    Y = df.iloc[1:len(df),5] 
    Y=Y.values.reshape(len(X),1).ravel()
    # Visualisation des données
    
    axes = plt.axes()
    axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
    plt.scatter(X,Y) # X et Y sont les variables extraites dans le paragraphe précédent
    plt.show()
    
    model = LinearSVR(epsilon=1.5,max_iter=1200000)


    # Entrainement du modèle
    model.fit(X, Y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y)
    
    y_pred=model.predict(X_test)
    
    print("Parametres du modele: ", model.get_params())

    #confusion matrix
    print(metrics.confusion_matrix(y_test, y_pred))
    '''
    disp = metrics.plot_confusion_matrix(model, X_test, y_test)     
    disp.figure_.suptitle("Confusion Matrix")
    print("Confusion matrix:\n%s" % disp.confusion_matrix)

    #score
    print("precision")
    print(precision_score(y_test, y_pred, average=None))

    print("rappel")
    print(recall_score(y_test, y_pred, average=None))

    print("F1")
    print(f1_score(y_test, y_pred, average=None))
'''

trainModel()
