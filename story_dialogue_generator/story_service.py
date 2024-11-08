import requests
from story_dialogue_generator.config import config

class StoryService:
    def __init__(self, user_session, title, settings, characters, plots=1, endings=1):
        """
        Inicializa la solicitud de historia con los detalles necesarios.

        :param user_session: Sesión de usuario para autenticación.
        :param title: Título de la historia (string).
        :param settings: Configuración de la historia (diccionario con "size" y "attributes").
        :param characters: Lista de personajes (lista de diccionarios con "name" y "attributes").
        :param plots: Número de tramas.
        :param endings: Número de finales.
        """
        self.user_session = user_session
        self.story_details = {
            "title": title,
            "settings": {
                "size": settings.get("size", "medium"),
                "attributes": settings.get("attributes", [])
            },
            "characters": [
                {
                    "name": char["name"],
                    "attributes": char.get("attributes", [])
                } for char in characters
            ],
            "plots": plots,
            "endings": endings
        }
        self.response = None

    def generate_story(self):
        url = f"{config.GENERATE_SERVICE_URL}/generate/story"

        # Enviar la solicitud con la estructura de story_details
        response = requests.post(
            url,
            json=self.story_details,  # Enviar story_details como JSON
            headers={"Authorization": f"Bearer {self.user_session.get_token()}"}
        )

        if response.status_code == 200:
            self.response = response.json()
        else:
            self.response = {
                "error": "Failed to generate story",
                "status_code": response.status_code,
                "details": response.text
            }

        return self.response
