import pandas as pd
from sklearn.linear_model import LinearRegression
data=pd.read_csv('data.csv')
X=data[['Hours_Studied']]
y=data['Marks']
model=LinearRegression()
model.fit(X,y)
hours=float(input("Enter Hours: "))
prediction=model.predict([[hours]])
print("prediction:",round(prediction[0],2))
