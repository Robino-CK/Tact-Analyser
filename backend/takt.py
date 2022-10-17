import simpleaudio as sa # # https://simpleaudio.readthedocs.io/en/latest/tutorial.html 
import time					
import threading


class Takt:
    # docu: https://simpleaudio.readthedocs.io/en/latest/simpleaudio.html
    def __init__(self, bpm):
        self.bpm = bpm
        self.audio_path = 'res/drum_stick.wav'  #sound origin: https://www.fesliyanstudios.com/royalty-free-sound-effects-download/drum-sticks-278
        self.wave_obj = sa.WaveObject.from_wave_file(self.audio_path)
    
    def play(self, anzahl):
        for i in range(anzahl):
            play_thread = threading.Thread(target=self.wave_obj.play)
            play_thread.start()
            time.sleep(60.0 / self.bpm)

    def stop(self):
        return
            
#takt = Takt(120)
#takt.play(10)



