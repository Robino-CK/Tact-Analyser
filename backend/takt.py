import math
from os import times
import numpy as np
import simpleaudio as sa # # https://simpleaudio.readthedocs.io/en/latest/tutorial.html 
import time					
base_tone = 'A', 4
tunning_Hz = 440
sa_timestemps = np.array([11025, 11025 * 2, 11025 * 4, 11025 * 8], np.int32)
tone_names = np.array(['C', 'CIS', 'D', 'DIS', 'E', 'F', 'FIS', 'G', 'GIS', 'A', 'AIS', 'B' ],  dtype=object)

def play_numpy(np_array):
    audio = np.hstack(np_array)   
    #audio *= 1 / 11025 * 1
    audio *= 32767 / np.max(np.abs(audio))     
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2,sa_timestemps[1])
    play_obj.wait_done()
    play_obj.stop()


class Tone:
    def __init__(self, tone = 'C', octave = 4):
        self.tone = tone
        self.octave = octave
        self.tone_length = 1
        self.set_index()
        self.set_frequenz()
        self.set_phase() # numpy array with phase. simpleaudio uses it!

    #useless:    
    def half_second(self, timestamp_array):
        index_of_array_ts = np.where(self.sa_timestemps == timestamp_array)
        return self.sa_timestemps.item(index_of_array_ts[0][0] - 1)

    def set_index(self):
        # index like = {0,1,2,...., 8*12 - 1} = {C_0, DIS_0,...., B_8}
        self.index = np.where(tone_names == self.tone)[0][0] + len(tone_names) * self.octave
   
    def set_frequenz(self):
        index_A_4 = np.where(tone_names == base_tone[0])[0][0] + len(tone_names) * base_tone[1]
        # do in A_4 
        distance_to_A_4 = self.index - index_A_4
        # fromular from: https://pages.mtu.edu/~suits/NoteFreqCalcs.html
        self.frequenz = ((2 ** (1/ 12)) **  distance_to_A_4) * tunning_Hz


    def set_phase(self):
        audio_array = np.linspace(0, self.tone_length, self.tone_length * sa_timestemps[3], False)
        self.phase = (np.sin(self.frequenz * audio_array * 2 * np.pi)  )
   
    def play(self):
        play_numpy(self.phase)
    
    
        

def play_tone():
    c = Tone()
    d = Tone('D')
    e = Tone('E')
    f = Tone('F')
    g = Tone('G')
    a = Tone('A')
    song = (c.phase, d.phase, e.phase, f.phase, g.phase,g.phase, a.phase, a.phase,  g.phase)
    wave = np.hstack(song)   
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


