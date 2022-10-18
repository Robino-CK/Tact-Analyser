
from asyncio.windows_events import NULL
import imp
from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QLabel, QLineEdit
import threading
from backend.takt import Takt   
from backend.recorder import Recorder
from gui.controll_line import Controll_Line
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 50)
        self.setWindowTitle('Takt Analyser')
        self.layout = QtWidgets.QVBoxLayout(self)
        c_line = Controll_Line(self)
        self.layout.addLayout(c_line)
        
    