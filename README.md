# voice-to-wav
A simple Python project to record audio from a microphone, save it as a .wav file, 
and subsequently use it for speech transcription via a separate model.

## Features:
- Records audio from the default system microphone outside the Docker container.
- Saves the recorded audio in the WAV file format.
- Audio processing and transcription inside the Docker container.
- Utilizes Poetry for dependency management.
- Containerized using Docker for easy deployment and scaling.

# Motivation:
Due to challenges in accessing the host machine's microphone directly from within a Docker container, 
the decision was made to handle audio recording outside the container and then process the audio inside. 
This workaround ensures compatibility and ease of deployment, especially when collaborating with multiple contributors.

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
        - `python main.py record` for recording
        - `python main.py process` for processing the recorded audio
    - Or, run the application using Poetry.
    - `poetry run python main.py record` or `poetry run python main.py process` 

## Docker instructions
- Build the Docker image.
    - `docker build -t voice-to-wav .`
    - This will build the Docker image with the name `voice-to-wav`.
- Run the Docker container.
- `docker run --rm voice-to-wav process`
   Note: Remember to record the audio outside the Docker container before processing it inside.

# Usage:
- Once the application starts with the record command, it will begin recording for a predefined duration (e.g., 5 seconds).
  After recording, it will automatically save the audio as an output.wav file in the voice directory.
- When using the process command, the application will use the saved .wav file and process it using the designated model 
  (currently placeholdered with m4t_predict).

# Contributing:
- Contributions are welcome! Please open an issue or submit a pull request on GitHub.