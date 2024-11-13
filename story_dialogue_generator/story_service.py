import requests
from story_dialogue_generator.config import config

class StoryService:
    def __init__(self, user_session, title, settings, characters, plots=1, endings=1):
        self.user_session = user_session
        self.story_details = {
            "title": title,
            "settings": {
                "size": settings.get("size", "medium"),
                "attributes": [
                    {"key": attr["key"], "value": attr["value"]}
                    for attr in settings.get("attributes", [])
                ]
            },
            "characters": [
                {
                    "name": char["name"],
                    "attributes": [
                        {"key": attr["key"], "value": attr["value"]}
                        for attr in char.get("attributes", [])
                    ]
                }
                for char in characters
            ],
            "plots": plots,
            "endings": endings
        }
        self.response = None

    def generate_story(self):
        url = f"{config.GENERATE_SERVICE_URL}/generate/story"

        response = requests.post(
            url,
            json=self.story_details,
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
