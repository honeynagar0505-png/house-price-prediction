import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\HONEY NAGAR\Documents\all python programs\Honey Nagar\HousePricePrediction\Housing.csv")
print(data.head())

print(data.isnull().sum())
data = data.dropna()

X = data[['area','bedrooms','bathrooms']]
y = data['price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train,y_test = train_test_split(
        X , y, test_size=0.2,random_state=42
)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test , predictions)
print("Error",mse)

new_house = np.array([[1600,3,2]])
price = model.predict(new_house)

print("Predicted Price:",price)

plt.scatter(data['area'],data['price'])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()