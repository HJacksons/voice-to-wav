import pyaudio
import wave


class Recorder:
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
        self.frames = []
        self.audio = pyaudio.PyAudio()

    def start_recording(self):
        stream = self.audio.open(format=self.format, channels=self.channels, rate=self.rate,
                                 input=True, frames_per_buffer=1024)
        print("Recording...")
        for _ in range(0, int(self.rate / 1024 * 5)):
            data = stream.read(1024)
            self.frames.append(data)
        print("Finished recording.")
        stream.stop_stream()
        stream.close()
        self.audio.terminate()

    def get_frames(self):
        return self.frames
