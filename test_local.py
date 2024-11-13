from story_dialogue_generator import UserSession, DialogueService, StoryService

user_session = UserSession()

story_data = "A hero embarks on a journey to save the kingdom."
dialogue_context = "The hero meets the villain for the first time in an epic showdown."
settings_dialogue = {
    "location": "castle",
    "time_of_day": "night",
    "number_of_scenes": 3,
    "number_of_characters": 2
}
characters_dialogue = [
    {
        "name": "Hero",
        "role": "protagonist",
        "mood": "determined",
        "attributes": [
            {"key": "courage", "name": "courage", "value": "high"}
        ]
    },
    {
        "name": "Villain",
        "role": "antagonist",
        "mood": "menacing",
        "attributes": [
            {"key": "intelligence", "name": "intelligence", "value": "high"}
        ]
    }
]

dialogue_service = DialogueService(
    user_session, story_data, dialogue_context, settings_dialogue, characters_dialogue, dialogue_style="dramatic"
)
dialogue_response = dialogue_service.generate_dialogue()
print("Respuesta del diálogo:", dialogue_response)


# Datos de prueba para generar historia
title = "The Great Adventure"
settings_story = {
    "size": "large",
    "attributes": [
        {"key": "theme", "value": "courage"}
    ]
}
characters_story = [
    {
        "name": "Knight",
        "attributes": [
            {"key": "role", "value": "protector"}
        ]
    },
    {
        "name": "Wizard",
        "attributes": [
            {"key": "skill", "value": "magic"}
        ]
    }
]

story_service = StoryService(user_session, title, settings_story, characters_story)
story_response = story_service.generate_story()
print("Respuesta de la historia:", story_response)



""" 
from story_dialogue_generator import DialogueService, StoryService

# Generación de diálogo desde un archivo JSON
dialogue_service = DialogueService(json_path="./dialogue.json")
dialogue_response = dialogue_service.generate_dialogue()
print("Respuesta del diálogo:", dialogue_response)

"""