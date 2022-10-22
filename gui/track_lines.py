
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QStyle, QLabel, QLineEdit
import os
from backend.analyser import Analyser 
import config
from datetime import datetime

class Track_Lines(QtWidgets.QVBoxLayout):
    def __init__(self):
        super().__init__()
        for root, dirs, files in os.walk(config.user_res, topdown=False):
            for dir in dirs:
                self.addLayout(Track_Line(dir))


class Track_Line(QtWidgets.QHBoxLayout):
    def __init__(self, dir):
        super().__init__()
        self.analyser = Analyser(dir)
        date_obj = datetime.strptime(dir, config.foldername_date_format)
        self.date_str = date_obj.strftime("%d %b %Y, %H:%M:%S")
        self.addWidget(QtWidgets.QLabel(self.date_str))
        icon_show_plot = QtWidgets.QWidget().style().standardIcon(getattr(QStyle, "SP_FileDialogInfoView"))
      
        self.button_show_plot = QtWidgets.QPushButton(icon_show_plot, "")
        self.button_show_plot.clicked.connect(self.show_plot)
        self.addWidget(self.button_show_plot)
        
        
        
       
    
    @QtCore.Slot()
    def show_plot(self):
        self.plot = self.analyser.get_diagramm()
        self.plot.setWindowTitle(self.date_str)
        self.plot.show()
  
