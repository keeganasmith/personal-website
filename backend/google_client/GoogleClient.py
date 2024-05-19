import os
import requests
from dotenv import load_dotenv
load_dotenv()
class GoogleClient:
    def __init__(self, access_token, refresh_token = None): #TODO: implmement refresh logic
        self.access_token = access_token
        self.refresh_token = refresh_token
    def get_email(self):
        url = 'https://www.googleapis.com/oauth2/v3/userinfo'
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            return user_info["email"]
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")