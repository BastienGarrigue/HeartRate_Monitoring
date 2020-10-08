import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score, auc, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import cross_val_score, RandomizedSearchCV
from evalModel import eval_model

def trainModel():
        
    
    rf = RandomForestClassifier()
    knn = KNeighborsClassifier()
    lr = LogisticRegression()
    
    eval_model(rf, 'feature')
    #eval_model(knn, 'none')
    #eval_model(lr, 'coef')
    
trainModel()
