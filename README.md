# NASA GISTEMP Climate Score Prediction using Machine Learning

## Overview

This project predicts NASA's monthly GISTEMP climate score using machine learning algorithms and climate data from public sources. The predictions are updated daily using the latest available data and are accurate to six decimal places. The goal is to deliver the most accurate prediction for the monthly GISTEMP score.

## Features

- **Automated Data Collection**: Scrapes and gathers climate data from published sources daily.
- **Machine Learning Models**: Uses time series forecasting and regression models for prediction.
- **Real-Time Updates**: The model runs daily to provide up-to-date predictions based on the latest data.
- **Precision**: Predicts the GISTEMP score with six decimal place accuracy (e.g., 1.213805).
- **Final Submission**: The final prediction for the month is captured on the 27th at 8:00 PM EST.

## Project Structure

|-- data/ # Directory to store raw and processed data |-- models/ # Machine learning models and training scripts |-- logs/ # Logs of daily predictions and performance metrics |-- scripts/ | |-- data_scraper.py # Script for scraping climate data | |-- train_model.py # Script for training the machine learning model | |-- predict.py # Script for running daily predictions |-- README.md

markdown


## Getting Started

### Prerequisites

- Python 3.x
- Climate data sources (e.g., NOAA, NASA)
- API keys (if applicable for data sources)

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/nasa-climate-prediction.git
cd nasa-climate-prediction

    Install dependencies:

bash

pip install -r requirements.txt

Running the Project

    Collect Data:

Run the data scraper to gather the most recent climate data:

bash

python scripts/data_scraper.py

    Train the Model:

Train the machine learning model with the collected data:

bash

python scripts/train_model.py

    Make Predictions:

Schedule the script to run daily for real-time predictions:

bash

python scripts/predict.py

Results

The final prediction for NASA's GISTEMP score for each month will be logged with six decimal places accuracy. Predictions are submitted privately for evaluation against NASA's official score.

-------------------------------------------------------------------------------------------------------

Motorcycle Real-Time Status and Fault Monitoring System

This project is designed to monitor real-time status indicators and fault warnings from a motorcycle's CAN Bus or OBD-II interface. It displays key parameters such as engine status, battery voltage, oil pressure, and more via a user-friendly graphical interface. The system logs critical faults and warnings for future reference.
Features

    Real-Time Monitoring: Retrieves real-time data from the motorcycle's CAN Bus or OBD-II interface.
    Fault Warnings: Displays alerts for critical warnings such as:
        Engine status fault
        ABS warning (if available)
        Oil Pressure (over threshold)
        Battery Voltage (under threshold)
        Fuel Warning (low fuel level)
        Tire Pressure (low pressure) (if available)
        Temperature Alarms (engine or coolant system)
        Turn Signal Activation/Deactivation
    Logging: Logs all warnings and critical statuses to a file (motorcycle_monitor.log) for later review.
    Graphical Interface: A simple Tkinter-based interface to display real-time data and warnings.

Requirements

    Python 3.x
    OBD-II or CAN Bus adapter (USB, Bluetooth, or other supported interfaces)

Python Libraries

    obd: For OBD-II communication
    python-can: For CAN Bus communication
    tkinter: For the GUI interface
    logging: For logging faults and warnings

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/motorcycle-monitoring-system.git
cd motorcycle-monitoring-system

Install required Python packages: You can install the dependencies via pip:

bash

pip install obd python-can

Connect your hardware:

    Plug in your OBD-II or CAN Bus adapter to the motorcycle and your computer.
    For OBD-II Bluetooth adapters, ensure it is paired with your computer.

Adjust settings (if necessary):

    For OBD-II adapters, you may need to specify the correct port for your connection. Modify the following line in the code:

    python

obd_conn = obd.OBD(portstr='COM3')  # Replace COM3 with your actual port

For CAN Bus, ensure you are using the correct channel and bustype based on your hardware:

python

        can_bus = can.interface.Bus(channel='can0', bustype='socketcan')  # For Linux

Usage

    Run the script:

    bash

    python motorcycle_monitoring.py

    Monitor your motorcycle's status:
        The GUI will display real-time status indicators for engine, battery, oil pressure, and other available metrics.
        Any warnings will be highlighted in the GUI, and logs will be saved in motorcycle_monitor.log.

Example GUI

The real-time monitoring GUI will display:

    Engine status
    Battery voltage
    Oil pressure status
    (Additional indicators as available from the motorcycle)

Troubleshooting

    No OBD-II Adapters Found:
        Ensure the adapter is connected and recognized by your system.
        If using Bluetooth, make sure the device is paired and that the correct port is specified.

    CAN Bus Errors:
        Ensure the python-can library is installed.
        Verify the correct channel and bustype are used for your CAN Bus adapter.

---------------------------------------------------------------------------------------------

Marketplace Product Parser

This Python program allows users to scrape product details from one marketplace and upload them to another marketplace by simply providing a product link and category name. It automates the process of transferring product data between two marketplaces.
Features

    Scrapes product name, price, and description from the provided marketplace link.
    Allows user input for product link and category name.
    Automatically uploads the parsed product data to your marketplace.

Requirements

    Python 3.x
    requests library
    beautifulsoup4 library

Installation

    Clone the repository to your local machine:

    bash

git clone https://github.com/yourusername/marketplace-product-parser.git
cd marketplace-product-parser

Install the required Python libraries:

bash

    pip install -r requirements.txt

Usage

    Run the script:

    bash

python parser.py

Enter the product link and the category name when prompted:

bash

    Enter the product link: https://example.com/product/123
    Enter the category name: Electronics

    The program will fetch the product details and upload them to your marketplace.

Example

If you input:

    Product link: https://example.com/product/123
    Category name: Electronics

The program will scrape the product name, price, and description from the provided link and upload it under the Electronics category to your marketplace.

-----------------------------------------------------------------------------------------------------------

# AI Healthcare App

## Overview

The AI Healthcare App is a comprehensive solution designed to assist patients in recording their doctor visits, receiving personalized AI-generated medication recommendations, and visualizing trends in symptoms over time. The application integrates both front-end and back-end components, providing a seamless user experience and robust functionality.

## Features

- **User Authentication:** Secure login system to manage patient access.
- **Symptom Input:** Allows users to enter symptoms and receive AI-generated medication recommendations.
- **Data Visualization:** Displays trends and patterns of symptoms over time using interactive graphs.
- **Language Localization:** Supports multiple languages with dynamic UI updates.
- **Voice Input (Optional):** (Commented out) Allows users to input symptoms via voice recognition.
- **Real-time Data Processing:** Backend API for handling recommendation requests and managing data.

## Technologies Used

- **Front-End:** Python, Tkinter for GUI
- **Back-End:** Flask for API development
- **Data Visualization:** Matplotlib
- **Voice Recognition:** SpeechRecognition (Optional)
- **API Requests:** Requests

## Installation

To get started with the AI Healthcare App, follow these installation steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-healthcare-app.git
   cd ai-healthcare-app

    Install Dependencies

    Create a virtual environment (optional but recommended) and install the required Python packages:

    bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

If using voice recognition, you’ll also need to install additional packages:

bash

pip install SpeechRecognition pyaudio

Run the Application

Start the Flask server and the Tkinter application:

bash

    python app.py

Usage

    Login: Enter your username and password to access the application.
    Enter Symptom: Type your symptoms into the input field and click "Get Recommendation" to receive AI-generated medication recommendations.
    View Trends: Analyze symptom trends using the interactive graphs.
    Change Language: Select your preferred language from the dropdown menu for localized UI.

API Endpoints
/recommendation

    Method: POST

    Description: Receives symptom data and returns medication recommendations.

    Request Body:

    json

{
  "symptoms": "example symptoms"
}

Response:

json

    {
      "recommendation": "Recommended Medication for example symptoms: Example Medicine"
    }

UI Features

    User Authentication: Secure login screen with username and password fields.
    Symptom Entry: Text field for entering symptoms with a submit button.
    Data Visualization: Matplotlib-based graphs for visualizing symptom trends.
    Language Selection: Dropdown menu for changing the UI language.
    Voice Input (Optional): Button for recording symptoms via voice (currently commented out).

Troubleshooting

    ModuleNotFoundError: Ensure all dependencies are installed. Use pip install -r requirements.txt to install required libraries.
    Voice Recognition Issues: Verify microphone settings and ensure pyaudio is installed correctly.

--------------------------------------------------------------------------------------------------------------------

Stable Diffusion Bot
Overview

The Stable Diffusion Bot is a Python-based implementation that applies a stable diffusion algorithm to images. The bot processes incoming requests containing images, applies diffusion, and returns the processed images. This bot can be extended to handle more sophisticated diffusion algorithms and integrated into larger systems.
Features

    Stable Diffusion: Applies a Gaussian filter for diffusion effects.
    Request Handling: Fetches image data from a URL, processes it, and sends the results back to a specified URL.
    Modular Design: Easily customizable and extendable for different diffusion algorithms and additional functionality.

Requirements

    Python 3.x
    numpy
    scipy
    requests

Install the required packages using pip:

bash

pip install numpy scipy requests

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/stable-diffusion-bot.git
cd stable-diffusion-bot

Install dependencies:

bash

    pip install -r requirements.txt

Usage
Example Code

Here's an example of how to use the Stable Diffusion Bot:

python

import numpy as np

from stable_diffusion_bot import StableDiffusionBot

# Initialize the bot
bot = StableDiffusionBot()

# Example image (100x100 random values)
example_image = np.random.rand(100, 100).tolist()
request_data = {'image': example_image, 'result_url': 'http://example.com/result'}

# Process the image
response = bot.process_request(request_data)
print("Diffused Image:", response)

Handling Requests

To handle requests from a URL and respond with the processed image:

python

request_url = 'http://example.com/request'
bot.handle_request(request_url)

Implementation Details
StableDiffusionBot Class

    apply_diffusion: Applies a Gaussian filter to simulate the diffusion process.
    process_request: Processes the incoming image request, applies diffusion, and prepares the result.
    handle_request: Fetches request data from a URL, processes it, and posts the result to another URL.

--------------------------------------------------------------------------------------------------------------------

PDF to Excel/Google Sheets Parser

This project provides two different solutions for parsing PDF files and exporting the data to either an Excel spreadsheet (using Python) or directly to Google Sheets (using Google Apps Script).
Features

    PDF Parsing: Extracts text or specific fields from a collection of PDF files.
    Excel Output: Saves the parsed data into an Excel file using Python.
    Google Sheets Output: Saves the parsed data directly to a Google Sheets document using Google Apps Script.
    Folder Monitoring: The Python script checks a specified folder for new PDFs and processes them automatically.

Getting Started
Prerequisites

For the Python version:

    Python 3.x
    Required libraries: pandas, pdfplumber, openpyxl, os

For the Google Apps Script version:

    A Google Account
    Access to Google Drive and Google Sheets

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/pdf-parser.git
cd pdf-parser

Install the required Python libraries:

bash

    pip install pdfplumber pandas openpyxl

Usage
Python Version (Excel Output)

    Modify the scan_folder_and_save_to_excel() function to specify the folder path containing the PDFs and the desired output Excel file path.
    Run the Python script:

    bash

    python pdf_parser.py

    The script will scan the specified folder, parse the PDFs, and output the results to an Excel file.

Google Apps Script Version (Google Sheets Output)

    Create a new Google Sheet and open the Script Editor (Extensions > Apps Script).
    Copy and paste the Google Apps Script code into the editor.
    Modify the folder ID and sheet name in the script to match your environment.
    Set up a trigger in Google Apps Script to run the scanFolderAndSaveToSheet function automatically when new PDFs are added to the folder.

Python Example

Here's a snippet of the Python script that parses PDFs and saves the data to an Excel sheet:

python

import os
import pandas as pd
import pdfplumber

def parse_pdf(file_path):
    """Parse fields from PDF"""
    with pdfplumber.open(file_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        # Custom logic to extract fields
        parsed_data = {
            'Field1': extract_field_1(text),
            'Field2': extract_field_2(text),
        }
    return parsed_data

def scan_folder_and_save_to_excel(folder_path, excel_path):
    parsed_results = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            parsed_results.append(parse_pdf(file_path))
    
    df = pd.DataFrame(parsed_results)
    df.to_excel(excel_path, index=False)

# Example Usage
scan_folder_and_save_to_excel('path/to/pdf/folder', 'output.xlsx')

Google Apps Script Example

Here is a snippet of the Google Apps Script for parsing PDFs and saving data to Google Sheets:

javascript

function parsePDF(fileId) {
  var file = DriveApp.getFileById(fileId);
  var blob = file.getBlob();
  // Custom logic to parse PDF text
  var text = PDFParserApp.parseText(blob);
  
  return [extractField1(text), extractField2(text)];
}

function scanFolderAndSaveToSheet() {
  var folder = DriveApp.getFolderById('folderId');
  var files = folder.getFilesByType(MimeType.PDF);
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('PDF Data');
  var row = 1;
  
  while (files.hasNext()) {
    var file = files.next();
    var parsedData = parsePDF(file.getId());
    sheet.getRange(row, 1, 1, parsedData.length).setValues([parsedData]);
    row++;
  }
}

Customization

    You can customize the parsing logic based on the structure of your PDFs. Modify the extract_field_1 and extract_field_2 functions to match the fields you're extracting.
    For the Python version, you can use different libraries for Excel export like xlsxwriter or openpyxl depending on your needs.
