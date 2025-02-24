import requests
import json
import os

class APIHandler:
    def __init__(self):
        self.api_keys = self.load_api_keys()
    
    def load_api_keys(self):
        with open('.env') as f:
            return dict(line.strip().split('=') for line in f if line and not line.startswith('#'))

    def get(self, url, params=None):
        headers = {
            'Authorization': f"Bearer {self.api_keys.get('API_KEY')}"
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def post(self, url, data=None):
        headers = {
            'Authorization': f"Bearer {self.api_keys.get('API_KEY')}",
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def handle_error(self, error):
        # Implement error handling logic here
        print(f"Error: {error}")