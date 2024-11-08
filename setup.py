from setuptools import setup, find_packages

setup(
    name="story_dialogue_generator",
    version="1.0.0",
    description="Librería para generar diálogos e historias",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "story_dialogue_generator=story_dialogue_generator.main:main",
        ]
    },
)
