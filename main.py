from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model/model.joblib")

class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int

@app.post("/predict")
def predict_price(features: HouseFeatures):
    X = np.array([[features.area, features.bedrooms, features.bathrooms]])
    prediction = model.predict(X)
    return {"predicted_price": prediction[0]}
