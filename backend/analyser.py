
#analyse audio data
#https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
from datetime import datetime
import config
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
class Analyser():
    def __init__(self, folder_name):
        for root, _, files in os.walk(f"{config.user_res}/{folder_name}", topdown=False):
            for file in files:
                if config.audio_format in file:
                    self.audio_file = file
                elif  config.pickle_format in file:
                    self.takt_file = file
     

    def get_snyc_time(self, filename_audio, filename_takte):
        dt_obj_audio = datetime.strptime(filename_audio, config.filename_date_format)
        dt_obj_takte = datetime.strptime(filename_takte, config.filename_date_format)
        dt_obj_diff = dt_obj_audio - dt_obj_takte
        return dt_obj_diff.total_seconds()  
    
    def get_diagramm(self):
        sc = Diagramm(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        return sc


class Diagramm(FigureCanvasQTAgg):
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Diagramm, self).__init__(fig)