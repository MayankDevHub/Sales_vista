import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Loading the data
data = pd.read_csv('data/sales_data.csv')
data['Month'] = pd.to_datetime(data['Month'])
data['Month_Num'] = np.arange(len(data))

X = data[['Month_Num']]
y = data['Sales']

model = LinearRegression()
model.fit(X, y)

# Predicting next 6 months
future_months = np.arange(len(data), len(data)+6).reshape(-1, 1)
forecast = model.predict(future_months)
print(forecast)
