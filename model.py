# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler

dataset = pd.read_excel(r'C:\Users\anmol singh\Downloads\Deployment-flask-master\new_project_flask')


main_df = df.iloc[:,2:]

main_df['Gender'] = pd.factorize(main_df['Gender'])[0]

from sklearn.model_selection import train_test_split

X = main_df.iloc[:,:10].values
y = main_df.iloc[:,10].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




sc = StandardScaler()
X_train = pd.DataFrame(sc.fit_transform(X_train))
X_test = pd.DataFrame(sc.transform(X_test))

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score,classification_report
def print_score(clf, X_train, y_train, X_test, y_test, train=True):
    if train:
        pred = clf.predict(X_train)
        print("Train Result:\n================================================")
        print(f"Accuracy Score: {accuracy_score(y_train, pred) * 100:.2f}%")
        print("_______________________________________________")
        print("Classification Report:", end='')
#         print(f"\tPrecision Score: {precision_score(y_train, pred) * 100:.2f}%")
#         print(f"\t\t\tRecall Score: {recall_score(y_train, pred) * 100:.2f}%")
#         print(f"\t\t\tF1 score: {f1_score(y_train, pred) * 100:.2f}%")
        print(classification_report(y_train,pred))
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_train, pred)}\n")
        
    elif train==False:
        pred = clf.predict(X_test)
        print("Test Result:\n================================================")        
        print(f"Accuracy Score: {accuracy_score(y_test, pred) * 100:.2f}%")
        print("_______________________________________________")
        print("Classification Report:", end='')
        print(classification_report(y_test,pred))      
#         print(f"\tPrecision Score: {precision_score(y_test, pred) * 100:.2f}%")
#         print(f"\t\t\tRecall Score: {recall_score(y_test, pred) * 100:.2f}%")
#         print(f"\t\t\tF1 score: {f1_score(y_test, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_test, pred)}\n")




rand_forest = RandomForestClassifier(n_estimators=1000, random_state=42)
rand_forest.fit(X_train, y_train)



print_score(rand_forest, X_train, y_train, X_test, y_test, train=True)
print_score(rand_forest, X_train, y_train, X_test, y_test, train=False)
results_df


filename = 'pickle_model1.sav'
pickle.dump(rand_forest, open(filename, 'wb'))