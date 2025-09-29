import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(boston.data , columns = boston.feature_names)
df['PRICE'] = boston.target

# preprocess the data
print(df.isnull().sum())

# visualize tha data
plt.hist(df['PRICE'] , bins= 30 , edgecolor = ' black')
plt.title("Distribution of House Price")
plt.ylabel("Frequency")
plt.xlabel("Price")
plt.show()
corr = df.corr()
fig, ax = plt.subplots(figsize= (10 , 8)) 
cax = ax.matshow(corr, cmpa = "coolwarm")
plt.xticks(range(len(corr.columns)) , corr.columns , rotation =90)
plt.yticks(range(len(corr.columns)) , corr.columns)
fig.colobar(cax)
plt.title("Correlation Matrix" , pad = 20)
plt.show()

# split the data
X = df.drop("PRICE" , axis = 1)
y = df["PRICE"]
X_train , X_test , y_train , y_test = train_test_split (X , y , test_size = 0.2 , random_state =42)

# Train a Linear Regrasstion
model = LinearRegression() 
model.fit(X_train , y_train)

#Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test , y_test)
r2 = r2_score(y_test , y_pred)
print("Mean Squared Error (MSE) : " , mse)
print("R-squared (R^2) :" , r2)