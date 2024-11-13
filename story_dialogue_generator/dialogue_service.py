import requests
from story_dialogue_generator.config import config

class DialogueService:
    def __init__(self, user_session, story, dialogue_context, settings, characters, dialogue_style="casual"):
        self.user_session = user_session
        self.story = story
        self.dialogue_context = dialogue_context
        self.settings = settings
        self.characters = characters
        self.dialogue_style = dialogue_style
        self.response = None

    def generate_dialogue(self):
        url = f"{config.GENERATE_SERVICE_URL}/generate/dialog"
        data = {
            "story": self.story,
            "dialogue_context": self.dialogue_context,
            "settings": {
                "location": self.settings.get("location", "unknown"),
                "time_of_day": self.settings.get("time_of_day", "morning"),
                "number_of_scenes": self.settings.get("number_of_scenes", 1),
                "number_of_characters": self.settings.get("number_of_characters", len(self.characters))
            },
            "characters": [
                {
                    "name": char["name"],
                    "role": char.get("role", "character"),
                    "mood": char.get("mood", "neutral"),
                    "attributes": [
                        {
                            "key": attr.get("key", attr["name"]),
                            "name": attr["name"],
                            "value": attr["value"]
                        } for attr in char.get("attributes", [])
                    ]
                } for char in self.characters
            ],
            "dialogue_style": self.dialogue_style
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
