
# 
import streamlit as st
import requests

# Set up Streamlit UI
st.title("🏒 NHL Game Winner Predictor")
st.write("Enter team and player stats to predict the game winner!")

# User Inputs
avg_home_weight = st.number_input("Average Home Team Weight", value=190)
avg_away_weight = st.number_input("Average Away Team Weight", value=185)
avg_home_height = st.number_input("Average Home Team Height", value=72)
avg_away_height = st.number_input("Average Away Team Height", value=75)
avg_home_age = st.number_input("Average Home Team Age", value=25)
avg_away_age = st.number_input("Average Away Team Age", value=26)
num_LeftShot_home = st.number_input("Number of Left Shot Players in Home Team", value=10)
num_RightShot_home = st.number_input("Number of Right Shot Players in Home Team", value=10)
num_LeftShot_away = st.number_input("Number of Left Shot Players in Away Team", value=5)
num_RightShot_away = st.number_input("Number of Right Shot Players in Away Team", value=15)
num_CAN_home = st.number_input("Number of Canadian Players in Home Team", value=10) 
num_CAN_away = st.number_input("Number of Canadian Players in Away Team", value=9)
num_USA_home = st.number_input("Number of American Players in Home Team", value=5)
num_USA_away = st.number_input("Number of American Players in Away Team", value=6)
num_FIN_home = st.number_input("Number of Finnish Players in Home Team", value=2)
num_FIN_away = st.number_input("Number of Finnish Players in Away Team", value=10)
num_SWE_home = st.number_input("Number of Swedish Players in Home Team", value=3)
num_SWE_away = st.number_input("Number of Swedish Players in Away Team", value=2)
num_RUS_home = st.number_input("Number of Russian Players in Home Team", value=2)
num_RUS_away = st.number_input("Number of Russian Players in Away Team", value=3)
num_OTHER_home = st.number_input("Number of Other Players in Home Team", value=1)
num_OTHER_away = st.number_input("Number of Other Players in Away Team", value=1)



# Button to Submit Prediction
if st.button("Predict Winner"):
    API_URL = "https://your-flask-api-url.onrender.com/predict"  # Update this with your deployed Flask API URL
    data = {"features": 
            [avg_home_weight, avg_away_weight, 
             avg_home_height, avg_away_height, 
             avg_home_age, avg_away_age,
             num_LeftShot_home, num_RightShot_home,
             num_LeftShot_away, num_RightShot_away,
             num_CAN_home, num_CAN_away,
             num_USA_home, num_USA_away,
             num_FIN_home, num_FIN_away,
             num_SWE_home, num_SWE_away,
             num_RUS_home, num_RUS_away,
             num_OTHER_home, num_OTHER_away
            ]
           }
    
    response = requests.post(API_URL, json=data)
    prediction = response.json()["prediction"]

    # Display Result
    if prediction == 1:
        st.success("🏆 Home Team is Predicted to Win!")
    else:
        st.error("🚀 Away Team is Predicted to Win!")
