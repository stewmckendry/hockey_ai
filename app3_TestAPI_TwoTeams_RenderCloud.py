# Description: This script tests the Flask API by sending a POST request with example input features.
# Make sure the Flask API is running before running this script.
# The script sends a POST request to the /predict route of the Flask API with example input features.
# The Flask API will return a JSON response with the prediction (0 or 1) for the input features.
# The prediction is printed to the console.
# This function has been refactored from app1_TestAPI_LocalHost.py to send two team names (abbreviatinons) rather than full list of features
# The revised Flask API (app3_FlaskAPI_TwoTeams.py) will look up the team stats and generate the features from the team stats and then make a prediction
# This version of the two teams test script is for the Render cloud deployment of the Flask API

# Import the requests library to send HTTP requests
import requests

# Test the app1_FlaskAPI.py by calling the /predict route with example input features
# URL of the Flask API
# Changed the URL to the Render URL 
# Render --> app1_FlaskAPI.py is now hosted on the cloud (anyone can access API!)
url = "https://hockey-ai-two-teams.onrender.com/predict"

# Example input features to submit in the POST request
# Two teams are sent as input features
data = {"team1": "MTL", "team2": "TOR"}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Print the response from the Flask API
print(response.json())  # Expected output: {"prediction": TOR}
