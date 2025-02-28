# Description: This script tests the Flask API by sending a POST request with example input features.
# Make sure the Flask API is running before running this script.
# The script sends a POST request to the /predict route of the Flask API with two team names
# The Flask API will look up the team stats and generate the features from the team stats and then make a prediction
# The prediction is printed to the console.
# This version of the two teams test script is for the local host deployment of the Flask API

# Import the requests library to send HTTP requests
import requests

# Test the app1_FlaskAPI.py by calling the /predict route with example input features
# URL of the Flask API
url = "http://127.0.0.1:5000/predict"

# Example input features to submit in the POST request
# Two teams are sent as input features
data = {"home_team": "ANA", "away_team": "BOS"}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Print the raw response content for debugging
print("Response Content:", response.content)

# Print the response from the Flask API
try:
    print(response.json())  # Expected output: {"prediction": 1}
except requests.exceptions.JSONDecodeError as e:
    print("Error decoding JSON:", e)
