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
