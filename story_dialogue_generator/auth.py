import requests
import os
import time
from dotenv import load_dotenv
from story_dialogue_generator.config import config

load_dotenv()  # Cargar variables de entorno

class UserSession:
    def __init__(self):
        # Obtener credenciales del entorno o archivo .env
        self.username = os.getenv("LIBRARY_USERNAME")
        self.password = os.getenv("LIBRARY_PASSWORD")

        if not self.username or not self.password:
            raise Exception("Credenciales no configuradas. Define LIBRARY_USERNAME y LIBRARY_PASSWORD en .env.")

        self.token = None
        self.token_expiration = None
        self.token_file = ".session_token"

        # Intentar cargar token desde archivo o autenticar
        self.load_token_from_file()
        if not self.token or time.time() >= self.token_expiration:
            self.authenticate()

    def authenticate(self):
        url = f"{config.USER_SERVICE_URL}/auth/token"
        response = requests.post(url, data={"username": self.username, "password": self.password})

        if response.status_code == 200:
            response_data = response.json()
            self.token = response_data.get("access_token")
            self.token_expiration = time.time() + 30 * 60  # Token válido por 30 minutos
            self.save_token_to_file()
        else:
            error_detail = response.json().get("detail", "Error desconocido")
            raise Exception("Error al autenticar usuario: " + error_detail)

    def save_token_to_file(self):
        with open(self.token_file, "w") as file:
            file.write(self.token + "\n" + str(self.token_expiration))

    def load_token_from_file(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, "r") as file:
                self.token = file.readline().strip()
                self.token_expiration = float(file.readline().strip())

    def get_token(self):
        if not self.token or time.time() >= self.token_expiration:
            self.authenticate()
        return self.token
