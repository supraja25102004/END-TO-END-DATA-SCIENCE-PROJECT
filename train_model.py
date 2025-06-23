import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset
data = pd.read_csv("data/housing.csv")
X = data[["area", "bedrooms", "bathrooms"]]
y = data["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.joblib")
print("Model trained and saved!")
 