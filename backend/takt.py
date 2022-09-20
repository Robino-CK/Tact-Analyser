import math
from os import times
import numpy as np
import simpleaudio as sa
# https://simpleaudio.readthedocs.io/en/latest/tutorial.html 
octave_4 = {"C": 261.63,"CIS" : 277.18, "D": 293.66, "DIS": 311.13, 
"E":329.63, "F": 349.23, "FIS": 369.99, "G": 392.00 ,  "GIS": 415.30, "A": 440.0, "AIS": 466.16, "B": 493.88}

class Tone:
    sa_timestemps = np.array([11025, 11025 * 2, 11025 * 4, 11025 * 8], np.int32)
    # tone_length must be value like 0.125,0.25,0,5,1,2,4,...
    def __init__(self, tone_length, frequenz):
        self.tone_length = tone_length
        self.frequenz = frequenz
        if (tone_length == 1):
            self.simple_audio_stamps = self.sa_timestemps[1]
        self.calculate_wave()

    
    def half_second(self, timestamp_array):
        index_of_array_ts = np.where(self.sa_timestemps == timestamp_array)
        return self.sa_timestemps.item(index_of_array_ts[0][0] - 1)

    def calculate_wave(self):
        audio_array = np.linspace(0, self.tone_length, self.tone_length * self.sa_timestemps[1], False)
        self.wave = (np.sin(self.frequenz * audio_array * 2 * np.pi)  )
    
    def calculate_audio_array(self):
        self.calculate_wave()
        audio = np.hstack((self.wave))   
        audio *= 32767 / np.max(np.abs(audio))     
        audio = audio.astype(np.int16)
        self.audio = audio

    def play(self):
        # start playback
        play_obj = sa.play_buffer(self.audio, 1, 2,self.sa_timestemps[3])
        
        # wait for playback to finish before exiting
        play_obj.wait_done()
    
        

class Song:
    def play_alle_meine_endchen(self):
        c =  Tone(1,octave_4["C"])
        d = Tone(1,octave_4["D"])
        e = Tone(1,octave_4["E"])
        f = Tone(1,octave_4["F"])
        g = Tone(1,octave_4["G"])
        a = Tone(1,octave_4["A"] )
        audio = np.hstack((c.wave, d.wave, e.wave, f.wave, g.wave,g.wave, a.wave, a.wave,  g.wave))   
        audio *= 32767 / np.max(np.abs(audio))     
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2,11025 * 4)
        play_obj.stop()
        play_obj.wait_done()

        return
def play_tone():
    song = Song()
    song.play_alle_meine_endchen()
    #tone = Tone(1,octave_4["C"])
    #tone.play()
# calculate note frequencies
#a_req = 440
play_tone()
#chr_freq = a_req * 2 ** (4 / 12)
#e_freq = a_req * 2 ** (7 / 12)
#song = Song()
#song.play_alle_meine_endchen()
#tone = Tone(1,chr_freq)
#tone.play()

#tone = Tone(1,e_freq)
#tone.play()


