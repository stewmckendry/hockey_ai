# Description: Streamlit GUI for NHL Game Winner Predictor
# User can input two NHL teams to predict the game winner
# The input features are sent to the deployed Flask API for prediction
# The prediction is displayed to the user in the Streamlit UI


# Potential future improvements:
# On the app, have user pick a team - both home and away - and then pre-load the feature values for each team, 
# and run the prediction


# Import Libraries
import streamlit as st
import requests

# Set up Streamlit UI
st.title("🏒 NHL Game Winner Predictor")
st.write("Enter two NHL teams to predict the game winner!")

# User Inputs
home_team = st.text_input("Home Team Name", value="Home Team")
away_team = st.text_input("Away Team Name", value="Away Team")

# Button to Submit Prediction
if st.button("Predict Winner"):

    # Prepare Data for Prediction
    # API URL is the Flask API deployed on Render
    # API leverages gunicorn to run the Flask app
    API_URL = "https://hockey-ai-two-teams.onrender.com/predict"  # Update this with your deployed Flask API URL
    
    # Prepare the input features as a dictionary
    data = {
        "home_team": home_team,
        "away_team": away_team
    }
    
    # Send a POST request to the API
    response = requests.post(API_URL, json=data)

    # Get the prediction from the JSON response
    response_json = response.json()

    # Handle API response
    if "prediction" in response_json:
        st.success(f"Predicted Winner: {response_json['prediction']}")
    else:
        st.error(f"Error: {response_json.get('error', 'Unknown error')}")

    