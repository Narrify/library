from story_dialogue_generator import UserSession, DialogueService, StoryService

# Autenticación del usuario
try:
    user_session = UserSession("nuevo_usuario", "nueva_contraseña")
    print("Autenticación exitosa, token obtenido:", user_session.get_token())
except Exception as e:
    print("Error en la autenticación:", e)
    exit()

# Configuración para generar un diálogo
story = "Esta es una historia de prueba para generar un diálogo."
dialogue_settings = {"number_of_scenes": 3, "number_of_characters": 2}
dialogue_characters = [
    {"name": "Alice", "attributes": [{"name": "age", "value": "30"}, {"name": "skill", "value": "negotiation"}]},
    {"name": "Bob", "attributes": [{"name": "age", "value": "35"}, {"name": "skill", "value": "combat"}]}
]

# Generación de diálogo
try:
    dialogue_service = DialogueService(user_session, story, dialogue_settings, dialogue_characters)
    dialogue_response = dialogue_service.generate_dialogue()
    print("Respuesta del diálogo:", dialogue_response)
except Exception as e:
    print("Error en la generación de diálogo:", e)

# Configuración para generar una historia
title = "La Aventura Inesperada"
story_settings = {
    "size": "medium",
    "attributes": [{"name": "theme", "value": "courage"}, {"name": "setting", "value": "medieval"}]
}
story_characters = [
    {"name": "Arthur", "attributes": [{"name": "role", "value": "knight"}, {"name": "skill", "value": "swordsmanship"}]},
    {"name": "Merlin", "attributes": [{"name": "role", "value": "wizard"}, {"name": "skill", "value": "magic"}]}
]
plots = 1
endings = 1

# Generación de historia
try:
    story_service = StoryService(user_session, title, story_settings, story_characters, plots, endings)
    story_response = story_service.generate_story()
    print("Respuesta de la historia:", story_response)
except Exception as e:
    print("Error en la generación de historia:", e)
