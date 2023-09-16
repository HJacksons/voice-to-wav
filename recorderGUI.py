import pyaudio

class Recorder:
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.recording = False
        self.stream = None

    def start_recording(self):
        self.stream = self.audio.open(format=self.format, channels=self.channels, rate=self.rate,
                                      input=True, frames_per_buffer=1024)
        print("Recording...")
        self.recording = True
        while self.recording:
            data = self.stream.read(1024)
            self.frames.append(data)

    def stop_recording(self):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        print("Stopped recording.")

    def get_frames(self):
        return self.frames
