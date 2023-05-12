import tkinter as tk
import pyaudio
import wave
import threading
import os

class App:
    def __init__(self, master):
        self.is_recording = False
        self.filename = "output.wav"
        self.record_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.record_button.pack()
        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state="disabled")
        self.stop_button.pack()

    def create_output_directory(self):
        directory = "audio_files"
        if not os.path.exists(directory):
            os.makedirs(directory)


    def start_recording(self):
        self.is_recording = True
        self.record_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.record_audio()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def get_unique_filename(self, base_filename):
        directory = "audio_files"
        counter = 1
        unique_filename = os.path.join(directory, base_filename)
        base_name, extension = os.path.splitext(base_filename)

        while os.path.exists(unique_filename):
            unique_filename = os.path.join(directory, f"{base_name}_{counter}{extension}")
            counter += 1

        return unique_filename

    def record_audio(self):
        self.create_output_directory()
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        frames = []

        def _record():
            while self.is_recording:
                data = stream.read(CHUNK)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            unique_filename = self.get_unique_filename(self.filename)
            wf = wave.open(unique_filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

        threading.Thread(target=_record).start()

root = tk.Tk()
root.geometry("300x100")
app = App(root)
root.mainloop()
