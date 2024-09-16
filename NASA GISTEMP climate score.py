import pandas as pd
import requests
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Constants
CLIMATE_DATA_URL = 'https://example.com/climate-data.csv'  # Replace with actual source
MODEL_PATH = 'models/climate_model.pkl'  # Corrected string
LOG_PATH = 'logs/predictions_log.csv'
DATA_DIR = 'data/'
MODEL_DIR = 'models/'
LOG_DIR = 'logs/'

# Create directories if they do not exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)


def download_climate_data():
    """Download and save the latest climate data as a CSV."""
    response = requests.get(CLIMATE_DATA_URL)
    filename = f"{DATA_DIR}climate_data_{datetime.now().strftime('%Y%m%d')}.csv"
    
    with open(filename, 'wb') as f:
        f.write(response.content)
    
    print(f"Downloaded climate data: {filename}")


def load_climate_data():
    """Load the latest climate data into a pandas DataFrame."""
    latest_file = sorted(os.listdir(DATA_DIR))[-1]  # Load the most recent file
    df = pd.read_csv(f"{DATA_DIR}{latest_file}")
    return df


def preprocess_data(df):
    """Preprocess the data for training or prediction."""
    # Drop rows with missing values
    df = df.dropna()

    # Example features: temperature, CO2 levels, sunspot numbers (replace with real columns)
    X = df[['temperature', 'co2_level', 'sunspot_number']]  # Add more features as needed
    y = df['gistemp_score']  # Target variable

    return X, y


def train_model(X, y):
    """Train a simple regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Using a simple Linear Regression model here
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the model to a file
    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved.")


def load_model():
    """Load the trained machine learning model."""
    if not os.path.exists(MODEL_PATH):
        print("Model not found. Please train the model first.")
        return None
    model = joblib.load(MODEL_PATH)
    return model


def make_prediction(model, latest_data):
    """Make predictions based on the latest data."""
    prediction = model.predict(latest_data)
    return prediction[0]


def log_prediction(prediction):
    """Log the prediction to a file."""
    with open(LOG_PATH, 'a') as f:
        log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {prediction:.6f}\n"
        f.write(log_line)
    print(f"Prediction logged: {prediction:.6f}")


def main():
    # Step 1: Download new climate data
    download_climate_data()

    # Step 2: Load and preprocess the data
    df = load_climate_data()
    X, y = preprocess_data(df)

    # Step 3: Train the model if it doesn't exist
    if not os.path.exists(MODEL_PATH):
        print("Training the model since no pre-trained model was found.")
        train_model(X, y)

    # Step 4: Load the trained model
    model = load_model()

    if model is None:
        return  # Exit if no model is loaded

    # Step 5: Make a prediction using the latest data
    prediction = make_prediction(model, X)

    # Step 6: Log the prediction
    log_prediction(prediction)


if __name__ == "__main__":
    main()
