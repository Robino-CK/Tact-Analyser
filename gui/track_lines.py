
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QStyle, QLabel, QLineEdit
import os
from backend.analyser import Analyser 
import config
from datetime import datetime

class Track_Lines(QtWidgets.QVBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        for root, dirs, files in os.walk(config.user_res, topdown=False):
            for dir in dirs:
                self.addLayout(self.get_line(dir))
                
    def get_line(self, dir):
        hline = QtWidgets.QHBoxLayout()
        analyser = Analyser(dir)
        
        date_obj = datetime.strptime(dir, config.foldername_date_format)
        date_str = date_obj.strftime("%d %b %Y, %H:%M:%S")
        hline.addWidget(QtWidgets.QLabel(date_str))
        hline.addWidget(analyser.get_diagramm())
        return hline

