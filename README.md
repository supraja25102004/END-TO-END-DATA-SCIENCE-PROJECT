# END-TO-END-DATA-SCIENCE-PROJECT
*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: ANKEPALLI SHIVA SUPRAJA

*INTERN ID*: CT08DN1734

*DOMAIN*: DATA SCIENCE

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

## Objective:

Develop a model that predicts house prices based on numerical features (area, number of bedrooms, number of bathrooms), and deploy it via an API using FastAPI so end-users or apps can get predictions in real-time.

## Folder Structure:

house_price_project/

├── app/

│ └── main.py # FastAPI app

├── data/

│ └── housing.csv # Sample dataset

├── model/

│ └── model.joblib # Trained ML model (generated)

├── train_model.py # Script to train and save the model

├── requirements.txt # Python dependencies

└── README.md # Project documentation

##  Workflow:

### Data Collection:

1.The dataset housing.csv contains structured housing data.

2.Features:

    area (in square feet)

    bedrooms (number of bedrooms)

    bathrooms (number of bathrooms)

3.Target variable: price (house price in dollars)

### Data Preprocessing:

1.Read the dataset using pandas.

2.Extract independent variables (X) and dependent variable (y):

    X = data[["area", "bedrooms", "bathrooms"]]
    
    y = data["price"]
    
3.No missing data, so imputation is not required.

4.Feature scaling is skipped as it's not critical for Linear Regression with similar numerical ranges.

### Model Building:

1.*Algorithm used*: Linear Regression

->Chosen for its simplicity and effectiveness in predicting continuous values.

->Assumes a linear relationship between features and target.

     model = LinearRegression()
     
     model.fit(X, y)

2.Model learns the coefficients (weights) to best fit the price based on the provided features.

### Model Evaluation:

For this small demo, no separate test set is used.

In a real-world scenario, you'd use:

     X_train, X_test, y_train, y_test = train_test_split(...)
     
and evaluate performance using metrics like R², MAE, or RMSE.

### Model Serialization:

Save the trained model using joblib:

       joblib.dump(model, "model/model.joblib")
       
This allows the model to be loaded and reused without retraining.

### Model Deployment (FastAPI):

A RESTful API is built using FastAPI, allowing users to send feature inputs and get real-time predictions.

The API:

->Accepts JSON input (area, bedrooms, bathrooms)

->Loads the pre-trained model

->Predicts and returns the price

#### Example API request:

    POST /predict
    {

          "area": 1800,
  
          "bedrooms": 4,
  
          "bathrooms": 2
          
     }
     
#### API response:

    {
    
         "predicted_price": 400000.0
         
    }
    
#### API Documentation:

FastAPI auto-generates documentation at:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## Dependencies:

#### requirements.txt:

    fastapi
    
    uvicorn
    
    scikit-learn
    
    pandas
    
    joblib


#### How to Install All Dependencies:

    pip install -r requirements.txt

#### Start FastAPI App:

Start the API server:

    uvicorn app.main:app --reload

## What Each Package Does:

*fastapi*->Web framework to create the REST API

*uvicorn*->ASGI server to run the FastAPI app

*scikit-learn*->Machine learning model training and prediction (Linear Regression)

*pandas*->Data loading and manipulation

*joblib*->Saving and loading the trained model efficiently

*numpy*->Handling numerical data (e.g., converting input into arrays for model)

## OUTPUT:

![Image](https://github.com/user-attachments/assets/519cdf45-1b1e-4650-b492-f3ef1663814f)






