# 🚀 This script creates a Flask web server that runs the trained mode
# Flask is a web framework for Python that allows you to create web servers - https://flask.palletsprojects.com/en/2.0.x/
# The web server will have two routes (API endpoints):
# - / : Home page
# - /predict : Predict game outcomes using the trained model
# The /predict route expects a POST request with a JSON body containing the features
# The model will return a JSON response with the prediction (0 or 1)   


# 🚀 Import the libraries
from flask import Flask, request, jsonify
import pickle
import numpy as np
import joblib

# Load the trained scaler so we can scale the input features like we did during training
scaler = joblib.load("scaler.pkl")

# 🚀 Load your trained model
with open("xgboost_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# create a Flask app (web server on localhost)
app = Flask(__name__)

# Define a route to the home page
@app.route("/")
def home():
    return "NHL AI Model is Running! Use /predict to get predictions."

# Define a route to predict game outcomes (i.e. run the AI model)
# This route expects a POST request with a JSON body containing the features
# The model will return a JSON response with the prediction
@app.route("/predict", methods=["POST"])
def predict():
    
     # ✅ Step 1: Receive and print incoming request data
    data = request.get_json()  # Get input from user
    print("Received Data:", data)  # Debugging: See what is sent to the API

    # ✅ Step 2: Convert JSON to NumPy array
    try:
        # Extract features from JSON and convert to NumPy array
        features = np.array(data["features"]).reshape(1, -1)  # Convert to NumPy array
        
        # ✅ Step 3: Scale the features
        features_scaled = scaler.transform(features)
        print("Processed Features:", features_scaled)  # Debugging: See formatted features
        
        # ✅ Step 4: Make a prediction
        prediction = model.predict(features_scaled)[0]  # Get prediction
        print("Model Prediction:", prediction)  # Debugging: See raw model output
        
        # ✅ Step 5: Return the prediction as a JSON response
        return jsonify({"prediction": int(prediction)})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Invalid input format"})
# Run the app
if __name__ == "__main__":
    app.run(debug=True)
