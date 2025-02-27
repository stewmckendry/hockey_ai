# Description: Streamlit GUI for NHL Game Winner Predictor
# User can input team and player stats to predict the game winner
# The input features are sent to the deployed Flask API for prediction
# The prediction is displayed to the user in the Streamlit UI
# The user can click a button to submit the prediction request
# The same Flask API from app1_Flask.py is used to make predictions
# The API URL is updated to the deployed API URL on Render
# This script can be run locally (streamlit run app2_StreamlitGUI.py) or can be deployed to Cloud (Streamlit Cloud)

# Import Libraries
import streamlit as st
import requests

# Set up Streamlit UI
st.title("🏒 NHL Game Winner Predictor")
st.write("Enter team and player stats to predict the game winner!")

# User Inputs
# Copilot Edit automatically changed from input to slider 
avg_home_weight = st.slider("Average Home Team Weight", min_value=150, max_value=250, value=190)
avg_away_weight = st.slider("Average Away Team Weight", min_value=150, max_value=250, value=185)
avg_home_height = st.slider("Average Home Team Height", min_value=60, max_value=80, value=72)
avg_away_height = st.slider("Average Away Team Height", min_value=60, max_value=80, value=75)
avg_home_age = st.slider("Average Home Team Age", min_value=18, max_value=40, value=25)
avg_away_age = st.slider("Average Away Team Age", min_value=18, max_value=40, value=26)
num_LeftShot_home = st.slider("Number of Left Shot Players in Home Team", min_value=0, max_value=20, value=10)
num_RightShot_home = st.slider("Number of Right Shot Players in Home Team", min_value=0, max_value=20, value=10)
num_LeftShot_away = st.slider("Number of Left Shot Players in Away Team", min_value=0, max_value=20, value=5)
num_RightShot_away = st.slider("Number of Right Shot Players in Away Team", min_value=0, max_value=20, value=15)
num_CAN_home = st.slider("Number of Canadian Players in Home Team", min_value=0, max_value=20, value=10) 
num_CAN_away = st.slider("Number of Canadian Players in Away Team", min_value=0, max_value=20, value=9)
num_USA_home = st.slider("Number of American Players in Home Team", min_value=0, max_value=20, value=5)
num_USA_away = st.slider("Number of American Players in Away Team", min_value=0, max_value=20, value=6)
num_FIN_home = st.slider("Number of Finnish Players in Home Team", min_value=0, max_value=20, value=2)
num_FIN_away = st.slider("Number of Finnish Players in Away Team", min_value=0, max_value=20, value=10)
num_SWE_home = st.slider("Number of Swedish Players in Home Team", min_value=0, max_value=20, value=3)
num_SWE_away = st.slider("Number of Swedish Players in Away Team", min_value=0, max_value=20, value=2)
num_RUS_home = st.slider("Number of Russian Players in Home Team", min_value=0, max_value=20, value=2)
num_RUS_away = st.slider("Number of Russian Players in Away Team", min_value=0, max_value=20, value=3)
num_OTHER_home = st.slider("Number of Other Players in Home Team", min_value=0, max_value=20, value=1)
num_OTHER_away = st.slider("Number of Other Players in Away Team", min_value=0, max_value=20, value=1)

# Button to Submit Prediction
if st.button("Predict Winner"):

    # Prepare Data for Prediction
    # API URL is the Flask API deployed on Render
    # API leverages gunicorn to run the Flask app
    API_URL = "https://hockey-ai.onrender.com/predict"  # Update this with your deployed Flask API URL
    
    # Prepare the input features as a dictionary
    data = {
        "features": [
            avg_home_weight, avg_away_weight, avg_home_height, avg_away_height, avg_home_age, avg_away_age,
            num_LeftShot_home, num_RightShot_home, num_LeftShot_away, num_RightShot_away,
            num_CAN_home, num_CAN_away, num_USA_home, num_USA_away,
            num_FIN_home, num_FIN_away, num_SWE_home, num_SWE_away,
            num_RUS_home, num_RUS_away, num_OTHER_home, num_OTHER_away
        ]
    }
    
    # Send a POST request to the API
    response = requests.post(API_URL, json=data)

    # Get the prediction from the JSON response
    prediction = response.json()["prediction"]

    # Display Result
    if prediction == 1:
        st.success("🏆 Home Team is Predicted to Win!")
    else:
        st.error("🚀 Away Team is Predicted to Win!")
