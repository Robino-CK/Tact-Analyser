
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QStyle, QLabel, QLineEdit
import threading
from backend.takt import Takt   
from backend.recorder import Recorder
import os 

audio_directory = 'res/recorded_audios/'


class Track_Lines(QtWidgets.QVBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        for root, _, files in os.walk(audio_directory, topdown=False):
            for name in files:
                self.get_line(root , name)
                
    def get_line(self, audio_path, audio_name):
        hline = QtWidgets.QHBoxLayout()
       # bpm = (int) (audio_name.split("B")[1].replace(".wav", ""))
        
        return    

