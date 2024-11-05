from setuptools import setup, find_packages

setup(
    name="story_dialogue_generator",
    version="0.1.0",
    description="A library for generating stories and dialogues",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jefferson Kevin", # xd
    author_email="yofer.corne@utec.edu.pe",
    url="https://github.com/Narrify/library",
    packages=find_packages(),  # Automatically finds the package folder
    install_requires=[
        "requests"  # Add any other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
