import re
import sounddevice as sd
from scipy.io.wavfile import write


def start_recorder():
    rec = Recorder()
    


class Recorder:
    def __init__(self, time_in_seconds = 3):
        self.time_in_seconds = time_in_seconds
        sample_rate = 44100
        myrecording = sd.rec(int(time_in_seconds * sample_rate), samplerate=sample_rate, channels=2)
        sd.wait()  # Wait until recording is finished
        write('res/asd.wav', sample_rate, myrecording)  # Save as WAV file 


