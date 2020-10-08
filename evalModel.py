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
# Bug quand c'était à l'interieur de la fct (test pour voir si ca marche)
columns = ['bpm', 'ibi','sdnn','sdsd','rmssd','Etat']
name="datasetv1.csv"
df = pd.read_csv(name, names=columns)
features = df.drop('Etat',axis=1)
labels = df["Etat"]

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25,shuffle=True,random_state=42)
plt.figure(figsize=(4,4))
plt.title("Dataset balance")
sns.countplot(df['Etat'])
    
    
correlation = df.corr()
plt.figure(figsize=(10,10))
plt.title("Features correlation")
sns.heatmap(correlation, annot=True,linewidths=3,cmap="YlGnBu")
print(df.head())

def eval_model(algo, m_type):

    print('---------------------------------------------------------------------')
    print('Model evaluation')
    print('---------------------------------------------------------------------')
    print(algo,'\n')
    
       
    
    # fit model
    algo.fit(X_train, y_train)
    accuracy = algo.score(X_test, y_test)
    scores = cross_val_score(algo, X_train, y_train, scoring='f1_macro', cv=5)
    print('Macro-F1 average: {0}'.format(scores.mean()))

    # Get prediction on test set
    y_pred = algo.predict(X_test)

    if m_type == 'coef':
        ft = algo.coef_.ravel()

    elif m_type == 'feature':
        ft = algo.feature_importances_


    # Get accuracy precision, recall & f1-score
    print('Accuracy:',accuracy)
    print('Classification report \n', classification_report(y_test, y_pred))

    # Confusion matrix
    plt.figure(figsize=(10,10))
    plt.subplot(321)
    plt.title('Confusion matrix')
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, linewidths=2)


    # Get ROC curve & AUC
    plt.subplot(322)
    predict_proba = algo.predict_proba(X_test)[:,1]
    fpr, tpr, thresholds = roc_curve(y_test, predict_proba)
    plt.plot(fpr, tpr, label=('Area under the curve :', auc(fpr, tpr)),color='g')
    plt.plot([1,0],[1,0],linestyle = "dashed")

    plt.legend(loc='best')
    plt.title('Roc curve & area under curve')
    # Get feature importances graph
    if m_type == 'feature' or m_type == 'coef':

        df = pd.DataFrame(ft, X_train.columns).reset_index()
        df = df.rename(columns={'index':'features',0:'coef'})
        df = df.sort_values(by='coef')

        plt.subplot(323)
        plt.title('Feature importances')
        sns.barplot(x='coef', y='features', data=df)
        plt.show()

    else :
        return algo  



    plt.tight_layout()