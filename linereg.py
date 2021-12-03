##################################################################################
# PROGRAM WILL GRAB PLAYER STATS FROM LOCAL PATH AND CREAT A LINEAR REGRESSION
# MODEL FOR ATTEPMTS AND COMPLETION PERCENTAGE FOR QUATERACKS ONLY

# ** WILL EVENTUALLY BE ABLE TO GRAB SPECIFIC PLAYER STATS **
# ** AND CREATE MODELS FOR THOSE STATS **
# test
##################################################################################
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# GRABS FROM THE EXCEL FILE
df = pd.read_excel(r"C:\Users\Giovannie\Desktop\dataproject\playerstats\statscrape.xlsx")

print()
year = int(input('What year would you want to begin at to look at Player Statistics?'))
print(str(year) + ' and the years after will be used for predictions...')

# GRABS NUMBER OF ATTEMPTS AND COMPLETION PERCENTAGES
y = np.array(df.loc[df["Season"] >= year, ['Cmp%']])
x = np.array(df.loc[df["Season"] >= year, ['Att']]).reshape((-1, 1))

# y = np.array(df['Cmp%'])
# x = np.array(df['Att']).reshape((-1, 1))

# GRABS THE MEAN AVERAGE OF EACH COLUMN THAT IS GRABBED
y_mean = np.array(df['Cmp%']).mean()
x_mean = np.array(df['Att']).mean()
print()
print('Mean of Cmp% : ', y_mean.round(3))
print('Mean of Att : ', x_mean.round(3))
# print(x.shape)
# print(y.shape)

##################################################################################
# FINDING THE MATHEMATICAL PORTIONS OF PREDICTIONS
model = LinearRegression().fit(x, y) 
print()
# Obtain the coefficient of determination
r_sq = model.score(x, y)
print('Coefficient of Determination:', r_sq.round(3))

# Print the Intercept:
print('Intercept:', model.intercept_.round(3))

# Print the Slope:
print('Slope:', model.coef_.round(3)) 
print()
# Prediction
y_pred = model.predict(x)
print('Predicted Completion Percentage:', y_pred.round(3), sep='\n')
# pred_mean = y_pred.mean()
# print('Mean of Prediction: ', pred_mean.round(3))
print()
##################################################################################
# SHOWING THE TRAINED X AND Y ON GRAPH
# model = LinearRegression(fit_intercept=True)
# model.fit(x[:, np.newaxis], y)
xfit = np.linspace(0, 800, 10)
yfit = model.predict(xfit[:, np.newaxis])

##################################################################################
# PRING OUT THE GRAPH 
plt.xlabel('Passing Attempts')
plt.ylabel('Completion percentage')
plt.scatter(x, y, color='c')
plt.plot(xfit, yfit, color='r');
plt.xlim([0, 700])
plt.ylim([0, 80])
plt.show()