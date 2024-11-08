import requests
from story_dialogue_generator.config import config

class DialogueService:
    def __init__(self, user_session, story, settings, characters):
        self.user_session = user_session
        self.story = story
        self.settings = settings
        self.characters = characters
        self.response = None

    def generate_dialogue(self):
        url = f"{config.GENERATE_SERVICE_URL}/generate/dialog"  
        data = {
            "story": self.story,
            "settings": {
                "number_of_scenes": self.settings["number_of_scenes"],
                "number_of_characters": self.settings["number_of_characters"]
            },
            "characters": [
                {
                    "name": char["name"],
                    "attributes": [{"name": attr["name"], "value": attr["value"]} for attr in char["attributes"]]
                } for char in self.characters
            ]
        }

        response = requests.post(
            url,
            json=data,
            headers={"Authorization": f"Bearer {self.user_session.get_token()}"}
        )

        if response.status_code == 200:
            self.response = response.json()
        else:
            self.response = {
                "error": "Failed to generate dialogue",
                "status_code": response.status_code,
                "details": response.text
            }

        return self.response
