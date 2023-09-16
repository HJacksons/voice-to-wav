import tkinter as tk
from recorderGUI import Recorder
from file_saver import FileSaver
import threading


class VoiceApp:
    def __init__(self, root):
        self.root = root
        self.rec = Recorder()

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack(pady=20)

        self.process_button = tk.Button(root, text="Process Audio", command=self.process_audio)
        self.process_button.pack(pady=20)

    def start_recording(self):
        if not self.rec.recording:
            t = threading.Thread(target=self.rec.start_recording)
            t.start()

    def stop_recording(self):
        if self.rec.recording:
            self.rec.stop_recording()
            frames = self.rec.get_frames()
            FileSaver.save_as_wav(frames)

    def process_audio(self):
        # Call your processing function here. For example, if in main.py you have:
        # process_audio('output.wav')
        pass


root = tk.Tk()
app = VoiceApp(root)
root.mainloop()
