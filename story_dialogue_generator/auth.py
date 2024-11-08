import requests
import time
from story_dialogue_generator.config import config

class UserSession:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.token_expiration = None
        self.authenticate()

    def authenticate(self):
        url = f"{config.USER_SERVICE_URL}/auth/token" 
        response = requests.post(url, data={"username": self.username, "password": self.password})

        if response.status_code == 200:
            response_data = response.json()
            self.token = response_data.get("access_token")
            self.token_expiration = time.time() + 30 * 60 
        else:
            raise Exception("Error al autenticar usuario: " + response.json().get("detail"))

    def get_token(self):
        if not self.token or time.time() >= self.token_expiration:
            self.authenticate()  
        return self.token
