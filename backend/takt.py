import math
from os import times
import numpy as np
import simpleaudio as sa
# https://simpleaudio.readthedocs.io/en/latest/tutorial.html 
class Tone:
    sa_timestemps = np.array([11025, 11025 * 2, 11025 * 4, 11025 * 8], np.int32)
    # tone_length must be value like 0.125,0.25,0,5,1,2,4,...
    def __init__(self, tone_length, frequenz):
        self.tone_length = tone_length
        self.frequenz = frequenz
        if (tone_length == 1):
            self.simple_audio_stamps = self.sa_timestemps[3]

    
    def half_second(self, timestamp_array):
        index_of_array_ts = np.where(self.sa_timestemps == timestamp_array)
        return self.sa_timestemps.item(index_of_array_ts[0][0] - 1)

    def calculate_wave(self):
        audio_array = np.linspace(0, self.tone_length, self.tone_length * self.sa_timestemps[1], False)
  
        self.wave = (np.sin(self.frequenz * audio_array * 2 * np.pi)  )

    def play(self):
        audio = np.hstack((self.wave))   
        audio *= 32767 / np.max(np.abs(audio))     
        audio = audio.astype(np.int16)
        # start playback
        play_obj = sa.play_buffer(audio, 1, 2,self.sa_timestemps[1])
        
        # wait for playback to finish before exiting
        play_obj.wait_done()

tone = Tone(1,440)
tone.calculate_wave()
tone.play()
# calculate note frequencies
a_req = 440
chr_freq = a_req * 2 ** (4 / 12)
e_freq = a_req * 2 ** (7 / 12)

