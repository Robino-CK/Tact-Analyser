import pyaudio
import wave
from datetime import datetime
import config
import os
#https://realpython.com/playing-and-recording-sound-python/ -> see Recoding Audio with pyaudio
class Recorder:
    def __init__(self):
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 1
        self.fs = 44100  # Record at 44100 samples per second
        self.seconds = 5
        

    def record(self, stop_event, folder_name):
       
        
        frames = self.get_audio_frames(stop_event)
        self.save_audio_frames(frames, folder_name)
        
    def get_audio_frames(self, stop_event):
        self.py_audio = pyaudio.PyAudio()  # Create an interface to PortAudio
        stream = self.py_audio.open(format=self.sample_format,
                channels=self.channels,
                rate=self.fs,
                frames_per_buffer=self.chunk,
                input=True)
        frames = []  # Initialize array to store frames
        dateTimeObj = datetime.now()
        self.filename = dateTimeObj.strftime(config.filename_date_format)
        while not stop_event.is_set():
            data = stream.read(self.chunk)
            frames.append(data)
       
        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        self.py_audio.terminate()
        return frames
    
    def save_audio_frames(self, frames, folder_name):
        dir = f"{config.user_res}{folder_name}"
        if not os.path.exists(dir):
            os.makedirs(dir) 
        filename =  self.filename  + config.audio_format
        path = dir +  "/" + filename
        wf = wave.open(path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.py_audio.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(frames))
        wf.close()
