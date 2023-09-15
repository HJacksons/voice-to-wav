import sys
import subprocess
from recorder import Recorder
from file_saver import FileSaver


def main(action):
    if action == "record":
        rec = Recorder()
        rec.start_recording()
        frames = rec.get_frames()
        FileSaver.save_as_wav(frames)
    elif action == "process":
        process_audio()
    else:
        print("Invalid action. Use 'record' or 'process'.")


def process_audio(audio_path="voice/output.wav"):
    # Using the provided audio path in the command
    cmd = ['m4t_predict', audio_path, 's2tt', 'eng', '--src_lang', 'eng']

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stderr)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please specify an action as an argument. Either 'record' or 'process'.")

#python main.py record && python main.py process