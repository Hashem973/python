import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {'Hours_Studied': [1, 2, 3, 4.5, 5.5, 6.1, 7.2, 8, 9],
        'Exam_Score':    [25, 35, 45, 52, 66, 70, 78, 85, 95]}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split input and output
X = df[['Hours_Studied']] 
y = df['Exam_Score']       

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict score for a new value, e.g., 10 hours
predicted_score = model.predict([[10]])
print(f"If a student studies for 10 hours, the predicted score is: {predicted_score[0]:.2f}")

# Plot the data and the regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Student Score Prediction')
plt.legend()
plt.grid(True)
plt.show()
