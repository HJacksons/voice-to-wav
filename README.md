# voice-to-wav
A simple Python project to record audio from a microphone and save it as a .wav file.
*I will use the .wav file as an input to my LLM for speech transcription*

## Features:
- Records audio from the default system microphone.
- Saves the recorded audio in the WAV file format.
- Utilizes Poetry for dependency management.
- Containerized using Docker for easy deployment and scaling.

## Installation:
### Prerequisites:
- Python 3.9+
- Docker (optional, if you want to run in a container)

## Steps:
- Clone the repository.
- Install the dependencies using Poetry.
   - `poetry install` (if you don't have Poetry installed, follow the instructions [here](https://python-poetry.org/docs/#installation))
- Run the application.
    - Activate the virtual environment created by Poetry.
        - `poetry shell`
        - `python main.py`
    - Or, run the application using Poetry.
    - `poetry run python main.py`

## Docker instructions
- Build the Docker image.
    - `docker build -t voice-to-wav .`
    - This will build the Docker image with the name `voice-to-wav`.
- Run the Docker container.
- `docker run --rm voice-to-wav`
   Note: Ensure your Docker environment has access to the system microphone.

# Usage:
- Once the application starts, it will begin recording for a predefined duration (e.g., 5 seconds). 
  After recording, it will automatically save the audio as an output.wav file in the project directory.

