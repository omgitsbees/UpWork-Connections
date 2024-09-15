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
