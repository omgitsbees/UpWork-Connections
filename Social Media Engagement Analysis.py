# Import libraries
import os
import schedule
import time
import pandas as pd
import logging
from dotenv import load_dotenv
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import plotly.express as px
from googleapiclient.discovery import build
import requests
import customtkinter as ctk
from tkinter import Tk, filedialog, Button

# Load environment variables for secure credential storage
load_dotenv()
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def log_message(message):
    logging.info(message)

# Function to fetch Twitter data (placeholder for actual API implementation)
def fetch_twitter_data(api_key, api_secret):
    log_message("Fetching Twitter data...")
    # Placeholder: Replace with actual Twitter API calls
    return [{"Date": "2024-11-15", "Platform": "Twitter", "Engagement": 120, "Likes": 80, "Shares": 40, "Comments": 10}]

# Function to fetch YouTube data
def fetch_youtube_data(api_key, channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw"):  # Default to Google Developers channel
    log_message("Fetching YouTube data...")
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(part="statistics", id=channel_id)
    response = request.execute()
    return [{"Date": "2024-11-15", "Platform": "YouTube", "Engagement": int(response['items'][0]['statistics']['viewCount']), "Likes": 500, "Shares": 100, "Comments": 50}]

# Analyze sentiment
def analyze_sentiment(text):
    log_message("Performing sentiment analysis...")
    return TextBlob(text).sentiment.polarity

# Predict engagement trends
def predict_engagement(data):
    log_message("Predicting engagement trends...")
    model = LinearRegression()
    X = data[['Likes', 'Shares']].values
    y = data['Comments'].values
    model.fit(X, y)
    predictions = model.predict(X)
    return predictions

# Visualize data with Plotly
def visualize_data(data):
    log_message("Visualizing data...")
    fig = px.bar(data, x='Date', y='Engagement', color='Platform', title='Engagement Trends')
    fig.show()

# Export data to various formats
def export_data(data, filename):
    log_message(f"Exporting data to {filename}...")
    df = pd.DataFrame(data)
    df.to_excel(f"{filename}.xlsx", index=False)
    df.to_json(f"{filename}.json", orient='records')

# Send data to CRM
def send_to_crm(data):
    log_message("Sending data to CRM...")
    url = "https://your-crm.com/api/leads"
    headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

# Schedule periodic updates
def job():
    twitter_data = fetch_twitter_data(TWITTER_API_KEY, TWITTER_API_SECRET)
    youtube_data = fetch_youtube_data(YOUTUBE_API_KEY)
    all_data = twitter_data + youtube_data
    export_data(all_data, "engagement_report")
    visualize_data(pd.DataFrame(all_data))
    log_message("Job completed successfully.")

schedule.every().day.at("10:00").do(job)

# GUI with CustomTkinter
def create_gui():
    log_message("Launching GUI...")
    app = ctk.CTk()
    app.geometry("400x300")
    app.title("Social Media Engagement Analyzer")

    def start_job():
        job()
        ctk.CTkLabel(app, text="Job executed! Check the logs for details.").pack(pady=10)

    def export_gui():
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if filepath:
            twitter_data = fetch_twitter_data(TWITTER_API_KEY, TWITTER_API_SECRET)
            youtube_data = fetch_youtube_data(YOUTUBE_API_KEY)
            all_data = twitter_data + youtube_data
            export_data(all_data, filepath)
            ctk.CTkLabel(app, text="Data exported successfully!").pack(pady=10)

    ctk.CTkButton(app, text="Run Analysis", command=start_job).pack(pady=10)
    ctk.CTkButton(app, text="Export Data", command=export_gui).pack(pady=10)
    app.mainloop()

# Start the GUI
if __name__ == "__main__":
    create_gui()
    while True:
        schedule.run_pending()
        time.sleep(1)
