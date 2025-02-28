# 🚀 This script creates a Flask web server that runs the trained mode
# Flask is a web framework for Python that allows you to create web servers - https://flask.palletsprojects.com/en/2.0.x/
# The web server will have two routes (API endpoints):
# - / : Home page
# - /predict : Predict game outcomes using the trained model
# The model converts the team names to team stats and then generates the features for the model to make a prediction
# The model will return a JSON response with the prediction (team name)  


# 🚀 Import the libraries
from flask import Flask, request, jsonify
import pickle
import numpy as np
import joblib
import pandas as pd

# Load the trained scaler so we can scale the input features like we did during training
scaler = joblib.load("scaler.pkl")

# 🚀 Load your trained model
with open("xgboost_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load team stats DataFrame (to look up features for inputted teams)
team_stats_df = pd.read_csv("team_stats.csv")

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
     # Inputs are two team names for prediction
     # Model expects team abbreviations in uppercase (e.g., "TOR" for Toronto Maple Leafs)
    data = request.get_json()  # Get input from user
    print("Received Data:", data)  # Debugging: See what is sent to the API

    # Check if the required keys are present in the request data
    if not data or "home_team" not in data or "away_team" not in data:
        return jsonify({"error": "Invalid input format. Please provide 'home_team' and 'away_team'."}), 400

    # Extract team names from JSON
    try:
        home_team = data["home_team"].upper()
        away_team = data["away_team"].upper()
    except AttributeError:
        return jsonify({"error": "Invalid input format. Team names must be strings."}), 400

    print("Received Data:", data, home_team, away_team)  # Debugging: See what is sent to the API

    # Lookup teams entered in CSV file based on team abbreviations
    home_stats = team_stats_df[team_stats_df["teamAbbrev"] == home_team]
    away_stats = team_stats_df[team_stats_df["teamAbbrev"] == away_team]
    print("Home team stats:", home_stats)  # Debugging: See home team stats
    print("Away team stats:", away_stats)  # Debugging: See away team stats

    # Ensure teams exist in the dataset
    if home_stats.empty or away_stats.empty:
        return jsonify({"error": "One or both team names not found"}), 400

    # Extract team stats from CSV file based on team abbreviations
    # These team stats are the features for the model to make a prediction
    feature_values = {
        "avg_home_weight": home_stats["avg_team_weight"].values[0],
        "avg_away_weight": away_stats["avg_team_weight"].values[0],
        "avg_home_height": home_stats["avg_team_height"].values[0],
        "avg_away_height": away_stats["avg_team_height"].values[0],
        "avg_home_age": home_stats["avg_team_age"].values[0],
        "avg_away_age": away_stats["avg_team_age"].values[0],
        "num_LeftShot_home": home_stats["num_LeftShot_players"].values[0],
        "num_RightShot_home": home_stats["num_RightShot_players"].values[0],
        "num_LeftShot_away": away_stats["num_LeftShot_players"].values[0],
        "num_RightShot_away": away_stats["num_RightShot_players"].values[0],
        "num_CAN_home": home_stats["num_CAN_players"].values[0],
        "num_CAN_away": away_stats["num_CAN_players"].values[0],
        "num_USA_home": home_stats["num_USA_players"].values[0],
        "num_USA_away": away_stats["num_USA_players"].values[0],
        "num_FIN_home": home_stats["num_FIN_players"].values[0],
        "num_FIN_away": away_stats["num_FIN_players"].values[0],
        "num_SWE_home": home_stats["num_SWE_players"].values[0],
        "num_SWE_away": away_stats["num_SWE_players"].values[0],
        "num_RUS_home": home_stats["num_RUS_players"].values[0],
        "num_RUS_away": away_stats["num_RUS_players"].values[0],
        "num_OTHER_home": home_stats["OTHER"].values[0],
        "num_OTHER_away": away_stats["OTHER"].values[0],
    }
    print(feature_values) # Debugging: See feature values


    # ✅ Step 2: Convert JSON to NumPy array
    try:
        # Extract features from JSON and convert to NumPy array
        features = np.array(list(feature_values.values())).reshape(1, -1)  # Convert to NumPy array
        
        # ✅ Step 3: Scale the features
        features_scaled = scaler.transform(features)
        print("Processed Features:", features_scaled)  # Debugging: See formatted features
        
        # ✅ Step 4: Make a prediction
        prediction_int = int(model.predict(features_scaled)[0])  # Get prediction
        print("Model Prediction:", prediction_int)  # Debugging: See raw model output
        
        # ✅ Step 5: Return the prediction as a JSON response
        # Convert prediction to human-readable format with team names
        prediction_team = home_team if prediction_int == 1 else away_team
        print("Model Prediction:", prediction_team)  # Debugging: See raw model output
        return jsonify({"prediction": prediction_team})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Invalid input format"})
# Run the app
if __name__ == "__main__":
    app.run(debug=True)
