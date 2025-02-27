# Description: This script tests the Flask API by sending a POST request with example input features.
# Make sure the Flask API is running before running this script.
# The script sends a POST request to the /predict route of the Flask API with example input features.
# The Flask API will return a JSON response with the prediction (0 or 1) for the input features.
# The prediction is printed to the console.

# Import the requests library to send HTTP requests
import requests

# Test the app1_FlaskAPI.py by calling the /predict route with example input features
# URL of the Flask API
url = "http://127.0.0.1:5000/predict"

# Example input features to submit in the POST request
# Copilot bug fix - each key, value pair needs a comma between them, not a : as suggested by Copilot
sample_features = [
    ('avg_home_weight', 100),
    ('avg_away_weight', 200),
    ('avg_home_height', 60),
    ('avg_away_height', 90),
    ('avg_home_age', 15),
    ('avg_away_age', 40),
    ('num_LeftShot_home', 10),
    ('num_RightShot_home', 10),
    ('num_LeftShot_away', 5),
    ('num_RightShot_away', 15),
    ('num_CAN_home', 10),
    ('num_CAN_away', 9), 
    ('num_USA_home', 5),
    ('num_USA_away', 6),
    ('num_FIN_home', 2),
    ('num_FIN_away', 10),
    ('num_SWE_home', 3),
    ('num_SWE_away', 2),
    ('num_RUS_home', 2),
    ('num_RUS_away', 3),
    ('num_OTHER_home', 1),
    ('num_OTHER_away', 1)
]  # Example input features

# Extract the feature values from the sample_features list
sample_feature_values = [value for _, value in sample_features]

# Create JSON data to send in the POST request with the input features
#data = {"features": sample_feature_values}  # Example input features
data = {"team1": "ANA", "team2": "BOS"}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Print the response from the Flask API
print(response.json())  # Expected output: {"prediction": 1}
