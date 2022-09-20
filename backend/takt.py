import math
from os import times
import numpy as np
import simpleaudio as sa
import time					
# https://simpleaudio.readthedocs.io/en/latest/tutorial.html 
octave_4 = {"C": 261.63,"CIS" : 277.18, "D": 293.66, "DIS": 311.13, 
"E":329.63, "F": 349.23, "FIS": 369.99, "G": 392.00 ,  "GIS": 415.30, "A": 440.0, "AIS": 466.16, "B": 493.88}
sa_timestemps = np.array([11025, 11025 * 2, 11025 * 4, 11025 * 8], np.int32)
tone_names = np.array(['C', 'CIS', 'D', 'DIS', 'E', 'F', 'FIS', 'G', 'GIS', 'A', 'AIS', 'B' ],  dtype=object)


def tone(tone_name, octave):
    index_of_tone = np.where(tone_names == tone_name)[0][0] 
    return tone_by_number(index_of_tone + len(tone_names) * octave)

def tone_by_number(tone_number):
    # tone_number = {0,1,2,...., 8*12} = {C_0, DIS_0,....}
    index_A_4 = np.where(tone_names == 'A')[0][0] + len(tone_names) * 4
    # do in A_4 
    distance_to_A_4 = tone_number - index_A_4
    # fromular from: https://pages.mtu.edu/~suits/NoteFreqCalcs.html
    return ((2 ** (1/ 12)) **  distance_to_A_4) * 440
    

def play_numpy(np_array):
    audio = np.hstack(np_array)   
    #audio *= 1 / 11025 * 1
    audio *= 32767 / np.max(np.abs(audio))     
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2,sa_timestemps[1])
    play_obj.wait_done()
    play_obj.stop()


class Tone:
    # tone_length must be value like 0.125,0.25,0,5,1,2,4,...
    def __init__(self, tone_length, frequenz):
        self.tone_length = tone_length
        self.frequenz = frequenz
        if (tone_length == 1):
            self.simple_audio_stamps = sa_timestemps[3]
        self.calculate_wave()

    
    def half_second(self, timestamp_array):
        index_of_array_ts = np.where(self.sa_timestemps == timestamp_array)
        return self.sa_timestemps.item(index_of_array_ts[0][0] - 1)

    def calculate_wave(self):
        audio_array = np.linspace(0, self.tone_length, self.tone_length * self.simple_audio_stamps, False)
        self.wave = (np.sin(self.frequenz * audio_array * 2 * np.pi)  )
    
    def play(self):
        play_numpy(self.wave)
    
        

def play_tone():
    fre = tone('D',4)
    c =  Tone(1,fre)
    d = Tone(1,octave_4["D"])
    e = Tone(1,octave_4["E"])
    f = Tone(1,octave_4["F"])
    g = Tone(1,octave_4["G"])
    a = Tone(1,octave_4["A"])
    song = (c.wave, d.wave, e.wave, f.wave, g.wave,g.wave, a.wave, a.wave,  g.wave)
    wave = np.hstack(song)   
    wave = np.hstack((song))
    tic = time.perf_counter() # Start Time
    play_numpy(wave)
    toc = time.perf_counter() # End Time
    # Print the Difference Minutes and Seconds
    print(f"wave length: {len(song)}")
    print(f"Build finished in {(toc - tic)} minutes {(toc - tic)%60:0.0f} seconds")
    # For additional Precision
    print(f"Build finished in {toc - tic:0.4f} seconds")

play_tone()


#chr_freq = a_req * 2 ** (4 / 12)
#e_freq = a_req * 2 ** (7 / 12)


