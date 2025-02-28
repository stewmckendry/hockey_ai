# Description: This script tests the Flask API by sending a POST request with example input features.
# Make sure the Flask API is running before running this script.
# The script sends a POST request to the /predict route of the Flask API with two team names
# The Flask API will look up the team stats and generate the features from the team stats and then make a prediction
# The prediction is printed to the console.
# This version of the two teams test script is for the cloud deployment of the Flask API

# Import the requests library to send HTTP requests
import requests

# Test the app3_FlaskAPI_TwoTeams.py by calling the /predict route with example input features
# URL of the Flask API
url = "https://hockey-ai-two-teams.onrender.com/predict"

# Example input features to submit in the POST request
# Two teams are sent as input features - hard coded for testing
data = {"home_team": "ANA", "away_team": "BOS"}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Print the raw response text for debugging
print("Raw API Response:", response.text)  # <-- This helps debug if response is not JSON

# Print the response from the Flask API
# Expected output: {"prediction": TOR}
try:
    prediction = response.json()["prediction"]
    print("Prediction:", prediction)
except requests.exceptions.JSONDecodeError:
    print("Error: API did not return valid JSON.")
  
