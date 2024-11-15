import json
import logging
import time
from typing import Dict, Any

# Import necessary libraries for API integration
from twilio.rest import Client as TwilioClient # Twilio for SMS
from sendgrid import SendGridAPIClient # SendGrid for email
from sendgrid.helpers.mail import Mail 

# Loggin Configuration 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example credentials (Replace with actual credentials)
TWILIO_SID = "your_twilio_account_sid"
TWILIO_TOKEN = "your_twilio_auth_token"
SENDGRID_API_KEY = "your_sendgrid_api_key"

# Initialize API clients
twilio_client = TwilioClient(TWILIO_SID, TWILIO_TOKEN)
sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)

def load_task_config(file_path: str) -> Dict[str, Any]:
    """Load tasks configuration from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)
    
def send_sms(params: Dict[str, Any]):
    """Send an SMS message using Twilio."""
    try:
        message = twilio_client.messages.create( 
            body=params["message"],
            from_='+your_twilio_number',
            to=params['to']
        )
        logging.info(f"SMS sent successfully: {message.sid}")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")

def send_email(params: Dict[str, Any]):
    """Send an email using SendGrid."""
    try:
        message = Mail(
            from_email='your_email@example.com',
            to_emails=params['to'],
            subject=params['subject'],
            html_content=params['content']
        )
        response = sendgrid_client.send(message)
        logging.info(f"Email sent successfully: {response.status_code}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def search_data(params: Dict[str, Any]):
    """Perform a data search or query (Placeholder function)."""
    # Example placeholder: Replace with actual data query logic
    query = params.get("query", "")
    logging.info(f"Searching for data with query: {query}")
    time.sleep(1) # Simulate data search
    logging.info(f"Data search completed for query: {query}")

def execute_task(task: Dict[str, Any]):
    """Execute a single task based on its name and parameters."""
    task_name = task['name']
    params = task['params']

    if task_name == 'send_sms':
        send_sms(params)
    elif task_name == 'send_email':
        send_email(params)
    elif task_name == 'search_data':
        search_data(params)
    else:
        logging.warning(f"Unknown task name: {task_name}")
    
def run_task_sequence(config: Dict[str, Any]):
    """Run a sequence of tasks defined in the configuration."""
    tasks = config.get('tasks', [])
    for task in tasks:
        try:
            logging.info(f"Starting task: {task['name']}")
            execute_task(task)
        except Exception as e:
            logging.error(f"Failed to execute task: {task['name']} - {e}")

if __name__ == "__main__":
    # Load task configuration
    config = load_task_config("tasks_config.json")
    # Execute the task sequence
    run_task_sequence(config)