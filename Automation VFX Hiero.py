import os
import shutil
import logging
from pathlib import Path
from airtable import Airtable
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
config = {
    "directories": ["/path/to/dir1", "/path/to/dir2"],  # Add your directories
    "destination_dir": "/path/to/save/exr",  # Destination directory for EXR files
    "airtable_api_key": "your_airtable_api_key",
    "airtable_base_id": "your_base_id",
    "airtable_table_name": "VFX Logs",
    "notification_email": "youremail@example.com",
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_username": "your_smtp_username",
    "smtp_password": "your_smtp_password",
}

# Logging setup
logging.basicConfig(
    filename="vfx_pull.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Airtable setup
airtable = Airtable(config["airtable_base_id"], config["airtable_table_name"], config["airtable_api_key"])

def notify_user(subject, body):
    """Sends an email notification."""
    try:
        msg = MIMEMultipart()
        msg["From"] = config["smtp_username"]
        msg["To"] = config["notification_email"]
        msg["Subject"] = subject 
        msg.attach(MIMEText(body, "plain"))

        with SMTP(config["smtp_server"], config["smtp_port"]) as server:
            server.starttls()
            server.login(config["smtp_username"], config["smtp_password"])
            server.send_message(msg)

        logging.info("Notification sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send notification: {e}")

def process_directory(directory, destination):
    """Processes a directory, copying EXR files to the destination."""
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".exr"):
                    source_path = Path(root) / file
                    dest_path = Path(destination) / file 
                    shutil.copy2(source_path, dest_path)
                    logging.info(f"Copied {source_path} to {dest_path}")
                    airtable.insert({"filename": file, "Source Path": str(source_path)})
    except Exception as e:
        logging.error(f"Error processing directory {directory}: {e}")
        notify_user(
            subject="VFX Automation Error",
            body=f"An error occurred while processing directory {directory}:\n{e}"
        )

def main():
    """Main script execution."""
    logging.info("Starting VFX pulling script.")
    try:
        Path(config["destination_dir"]).mkdir(parents=True, exist_ok=True)
        for directory in config["directories"]:
            if Path(directory).exists():
                process_directory(directory, config["destination_dir"])
            else:
                logging.warning(f"Directory does not exist: {directory}")
                airtable.insert({"Directory": directory, "Status": "Not Found"})

        notify_user(
            subject="VFX Automation Script Completed",
            body="The VFX pulling script has completed successfully."
        )
        logging.info("VFX pulling script completed.")
    except Exception as e:
        logging.critical(f"Critical error in the script: {e}")
        notify_user(
            subject="Critical Error in VFX Automation Script",
            body=f"A critical error occurred:\n{e}"
        )

if __name__ == "__main__":
    main()