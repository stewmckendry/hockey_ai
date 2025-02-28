# Description: This script creates a Telegram bot that allows users to get NHL game predictions.
# The bot has two commands: /start and /predict.
# The /start command displays a welcome message to the user.
# The /predict command takes two team names as arguments and sends a POST request to the Flask API to get a prediction.
# The prediction is then displayed to the user in the Telegram chat.
# The bot runs continuously and listens for user commands.
# The bot uses the python-telegram-bot library to interact with the Telegram API.
# The bot requires a Telegram Bot Token to authenticate with the Telegram API.
# The bot also requires the Flask API URL to send prediction requests.


# Import libraries
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

# Replace with your Telegram Bot Token (from Telegram App > FatherBot)
TELEGRAM_BOT_TOKEN = "7409084962:AAFvzSJdcavSXWFO5dsTFzJXTrTVEfy02UU"

# Replace with your actual Flask API URL (Flask API hosted on Render)
FLASK_API_URL = "https://hockey-ai-two-teams.onrender.com/predict"  # Replace with your actual Flask API URL

# Define the /start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome to NHL Predictor Bot! Type /predict Team1 Team2 to get a prediction.")

# Define the /predict command handler
# The /predict command takes two team names as arguments and sends a POST request to the Flask API to get a prediction
# Example usage: /predict TOR MTL  
async def predict(update: Update, context: CallbackContext) -> None:
    # Check if the user provided exactly two team names
    teams = context.args

    # Check if the user provided exactly two team names
    if len(teams) != 2:
        await update.message.reply_text("Please provide exactly two team names. Example: /predict Leafs Canadiens")
        return

     # API request
    try:
        # Send a POST request to the Flask API with the two team names
        response = requests.post(FLASK_API_URL, json={"home_team": teams[0], "away_team": teams[1]})

        # Debugging: Print full response in case of error
        print("API Response Status Code:", response.status_code)
        print("API Response Text:", response.text)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            prediction = response.json().get("prediction", "Could not retrieve prediction.")
            await update.message.reply_text(f"Prediction: {prediction}")
        else:
            await update.message.reply_text("Error: Could not connect to the prediction API.")
    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)
        await update.message.reply_text("Error: Could not connect to the prediction API.")  

# Main function to run the Telegram bot
def main():
    # Create a new Telegram Application with the bot token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add the /start and /predict command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("predict", predict))

    # Run the bot and listen for user commands
    application.run_polling()

# Run the main function
if __name__ == "__main__":
    main()
