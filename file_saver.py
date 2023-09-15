import wave
import pyaudio
import os

dire = "voice/"


class FileSaver:
    if not os.path.exists("voice"):
        os.makedirs("voice")

    @staticmethod
    def save_as_wav(frames, path=dire + "output.wav"):
        wf = wave.open(path, 'wb')
        wf.setnchannels(2)
        wf.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()
