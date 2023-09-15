FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml .

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libasound2-dev \
    portaudio19-dev \
    alsa-utils \
    pulseaudio \
    pulseaudio-utils && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

# Copy your scripts into the container
COPY . .

CMD ["python", "main.py", "process"]
#CMD ["tail", "-f", "/dev/null"] # Keep container running

