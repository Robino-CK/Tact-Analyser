
#analyse audio data
#https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
from datetime import datetime
import config
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import pickle
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
class Analyser():
    def __init__(self, folder_name):
        for root, _, files in os.walk(f"{config.user_res}/{folder_name}", topdown=False):
            self.root = root
            for file in files:
                if config.audio_format in file:
                    self.audio_file_name = file
                
                elif  config.pickle_format in file:
                    self.takt_file_name = file
                    with open(root + "/" + self.takt_file_name, 'rb') as handle:
                        self.takte = pickle.load(handle)
       
        
        
    def load_audio_data(self):
        self.audio_time_serie, self.audio_sample_rate = librosa.load(self.root + '/' + self.audio_file_name )
        self.tempo, self.beats = librosa.beat.beat_track(y= self.audio_time_serie, sr=self.audio_sample_rate)
        onset_env = librosa.onset.onset_strength(y=self.audio_time_serie, sr=self.audio_sample_rate, aggregate=np.median)
        hop_length = 512
        self.times = librosa.times_like(onset_env, sr=self.audio_sample_rate, hop_length=hop_length)

    def set_sync_takte(self):
        self.sync_takte = []
        sync_time = self.get_snyc_time()
        for t in self.takte:
            self.sync_takte.append(t - sync_time)
       


    def get_snyc_time(self):
        dt_obj_audio = datetime.strptime(self.audio_file_name.replace(".wav", ""), config.filename_date_format)
        dt_obj_takte = datetime.strptime(self.takt_file_name.replace(".pickle", ""), config.filename_date_format)
        dt_obj_diff = dt_obj_audio - dt_obj_takte
        return dt_obj_diff.total_seconds()  
    
    def get_diagramm(self):
        self.load_audio_data()
        self.set_sync_takte()
        sc = Diagramm(self, width=5, height=4, dpi=100)
        librosa.display.waveshow(self.audio_time_serie, sr=self.audio_sample_rate, alpha=0.5,ax=sc.axes,  label='Audio')  
        sc.axes.vlines(self.times[self.beats], -0.1, 0.1, alpha=1, color='r',

           linestyle='--', label='Dedected Beats')
     
        sc.axes.vlines(self.sync_takte, -0.1, 0.1, alpha=0.5, color='g',

                linestyle='--', label='Real Beats')

        sc.axes.legend()
        return sc


class Diagramm(FigureCanvasQTAgg):
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Diagramm, self).__init__(fig)