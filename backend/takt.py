import simpleaudio as sa # # https://simpleaudio.readthedocs.io/en/latest/tutorial.html 
import time					
import threading
from datetime import datetime
import pickle

class Takt:
    # docu: https://simpleaudio.readthedocs.io/en/latest/simpleaudio.html
    def __init__(self, bpm):
        self.stop = False
        self.bpm = bpm
        self.audio_path = 'res/drum_stick.wav'  #sound origin: https://www.fesliyanstudios.com/royalty-free-sound-effects-download/drum-sticks-278
        self.wave_obj = sa.WaveObject.from_wave_file(self.audio_path)
    
    def play(self, stop_event):
        frames = []
        start_time = time.time() 
        dateTimeObj = datetime.now()
        filename = dateTimeObj.strftime("%Y-%m-%d-%H-%M-%S-%f")  
        while not stop_event.is_set():
            time_stap = time.time() - start_time
            frames.append(time_stap)
            play_thread = threading.Thread(target=self.wave_obj.play)
            
            play_thread.start()
            
            time.sleep(60.0 / self.bpm)
        
        
        with open(f'res/recorded_takte/{filename}.pickle', 'wb') as handle:
            pickle.dump(frames, handle, protocol=pickle.HIGHEST_PROTOCOL)
   





