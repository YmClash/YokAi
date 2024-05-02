import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import jaccard_score, f1_score, log_loss, confusion_matrix, accuracy_score
import sklearn.metrics as metrics
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn


# on  telecharge  le dataset

DATASET = r'C:\Users\y_mc\PycharmProjects\YokAi\Dataset\Weather_Data.csv'

data = pd.read_csv(DATASET)
# print(data.columns)

#  on  traite et  normalise les data
data_sydney_procecced = pd.get_dummies(data,columns=['RainToday','WindGustDir','WindDir9am','WindDir3pm'])
data_sydney_procecced.replace(['No','Yes'],[0,1] ,inplace=True)
data_sydney_procecced.drop('Date',axis=1,inplace=True)
data_sydney_procecced = data_sydney_procecced.astype(float)

features = data_sydney_procecced.drop(columns='RainTomorrow', axis=1)
X = features
Y = data_sydney_procecced['RainTomorrow']

# on commence l'entrainement

x_train, x_test, y_train, y_test = train_test_split(X,Y ,test_size=0.2,random_state=10)

lm = LinearRegression()
lm.fit(X,Y)
resultat = lm.score(X,Y)

print(f'resultat Linear Regression: {resultat}')

#  on utilise la methode predict  sur le set x_test du dataset
prediction = lm.predict(x_test)
print(f'Resultat de la prediction :*** \n ')

# on  va utilise different metric enfin d'evalue notre prediction
# on calcule se different metrics  avec l'aide de y_test et  predict

LinearRegression_MAE = metrics.mean_absolute_error(y_test,prediction)
print(f'Mean Absolute Error:{LinearRegression_MAE}')

LinearRegression_MSE = metrics.mean_squared_error(y_test,prediction)
print(f'Mean Square Error:{LinearRegression_MSE}')

LinearRegression_R2 = metrics.r2_score(y_test,prediction)
print(f'R2 Score  Error: {LinearRegression_MAE}')

print("\n")

# on va transporte cela dans  un tableau

result = {"Metrics":["MAE","MSE","R2"],"Resultat":
    [LinearRegression_MAE,LinearRegression_MSE,LinearRegression_R2]}
Report = pd.DataFrame(result)

print(Report.head())
print("\n")
#  Create and train a KNN model called KNN using the training data
#  (x_train, y_train) with the n_neighbors parameter set to 4.

K_params = 4
KNN = KNeighborsClassifier(n_neighbors=K_params).fit(x_train,y_train)
# resultat_KNN = KNN.score(x_train,y_train)
# print(f'Resultat KNN: {KNN}')
knn_prediction = KNN.predict(x_test)
print(f'Resultat KNN_prediction:\n {knn_prediction[0:100]}')

print("\n")
# Using the predictions and the y_test dataframe
# calculate the value for each metric using the appropriate function.

# KNN accuracy Score
KNN_Accuracy_Score = accuracy_score(y_test,knn_prediction)
# train_set_accu = accuracy_score(y_train,KNN.predict(x_test))
print(f'KNN Test set Accuracy Score :{KNN_Accuracy_Score} \n ')

#  Jaccard Index
KNN_JaccardIndex = jaccard_score(y_test,knn_prediction)
print(f'KNN Test set Jaccard Score :{KNN_Accuracy_Score} \n')


#the F2 Index
KNN_F1_Score = f1_score(y_test,knn_prediction)
print(f'KNN Test set F1 Score : {KNN_F1_Score} ')


#Q9) Create and train a Decision Tree model called Tree using the training data (x_train, y_train).¶

Tree = DecisionTreeClassifier()
Tree.fit(x_train,y_train)
# Q10) Now use the predict method on the testing data (x_test) and save it to the array predictions.
PredTree = Tree.predict(x_test)


# Q11) Using the predictions and the y_test dataframe calculate the value
# for each metric using the appropriate function.
Tree_Accuracy_Score = accuracy_score(y_test,PredTree)
print(f'Tree Test set Accuracy Score: {Tree_Accuracy_Score}')
Tree_JaccardIndex = jaccard_score(y_test,PredTree)
print(f'Tree Test set Jaccard Index Score: {Tree_JaccardIndex}')
Tree_F1_Score = f1_score(y_test,PredTree)
print(f'Tree Test set F1 Score Score: {Tree_F1_Score}')

# Q12) Use the train_test_split function to split the features
# and Y dataframes with a test_size of 0.2 and the random_state set to 1.

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2,random_state=1)

# Q13) Create and train a LogisticRegression model called LR
# using the training data (x_train, y_train) with the solver parameter set to liblinear.

LR = LogisticRegression(solver="liblinear")
LR.fit(x_train,y_train)

# Q14) Now, use the predict and predict_proba methods on
# the testing data (x_test) and save it as 2 arrays predictions and predict_proba.

predict_log_reg = LR.predict(x_test)
predict_probaba = LR.predict_proba(x_test)

# Q15) Using the predictions, predict_proba and the y_test dataframe calculate the value for each metric using the appropriate function.

#Enter Your Code, Execute and take the Screenshot
LR_Accuracy_Score = accuracy_score(y_test,predict_log_reg)
print(f'Tree Test set Accuracy Score: {LR_Accuracy_Score}')
LR_JaccardIndex = jaccard_score(y_test, predict_log_reg ,pos_label = 0)
print(f'Tree Test set Accuracy Score: {LR_JaccardIndex}')
LR_F1_Score = f1_score(y_test, predict_log_reg)
print(f'Tree Test set Accuracy Score: {LR_F1_Score}')
LR_Log_Loss = log_loss(y_test,predict_probaba)
print(f'Tree Test set Accuracy Score: {LR_Log_Loss}')

#
# SVM
# Q16) Create and train a SVM model called SVM using the training data (x_train, y_train).

SVM = svm.SVC()
SVM.fit(x_train,y_train)








#
#
# print(data_sydney_procecced)
#

# print(data.columns)
# print(data.describe())

















# path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillUp/labs/ML-FinalAssignment/Weather_Data.csv'
# savepath =  Path(r'C:\Users\y_mc\PycharmProjects\YokAi\Dataset\Weather_Data.csv')
# dataset = pd.read_csv(path)
# dataset.to_csv(savepath)
