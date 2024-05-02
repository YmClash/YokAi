import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error ,mean_squared_error, r2_score
import sklearn.metrics as metrics


# Dataset_path = r'C:\Users\y_mc\PycharmProjects\YokAi\Dataset\Weather_Data.csv'
#
# data = pd.read_csv(Dataset_path)
#
# print(data.head())

#valeur reel

Y_true =[3,-0.5,3,8,12]

Y_pred = [2.5,0.0,4,7,10]

print(type(Y_pred))

mae = mean_absolute_error(Y_true,Y_pred)
mse = mean_squared_error(Y_true,Y_pred)
r2_score = r2_score(Y_true,Y_pred)
print(f'lerreur absolu moyenne : {mae}')
print(f'lerreur Quadratique moyenne : {mse}')
print(f'lerreur F1 Score : {r2_score}')