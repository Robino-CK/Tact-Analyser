
from asyncio.windows_events import NULL
from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QLabel, QLineEdit
import threading
from backend.takt import Takt   

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 100)
        self.create_takt_gui()

    def create_takt_gui(self):
        # flag to decide which state GUI is 
        self.is_running_takt = False
        
        self.layout = QtWidgets.QHBoxLayout(self)
        # start/stop - Button
        icon_play = self.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
        self.button_takt = QtWidgets.QPushButton(icon_play, "Start Takt")
        self.button_takt.clicked.connect(self.controll_takt)
        self.layout.addWidget(self.button_takt)
        # bpm - Input
        self.line_edit_bpm = QLineEdit()
        self.line_edit_bpm.setText("120")
        onlyInt = QIntValidator()
        self.line_edit_bpm.setValidator(onlyInt)
        self.layout.addWidget(self.line_edit_bpm)
        # bpm - Label
        self.text_bpm = QLabel("bpm")
        self.layout.addWidget(self.text_bpm)

        

    @QtCore.Slot()
    def controll_takt(self):
        if (self.is_running_takt):
            self.is_running_takt = False
            self.stop_takt() 
        else:
            self.is_running_takt = True
            self.start_takt()
            
    def stop_takt(self):
        icon_start = self.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
        self.button_takt.setText("Start Takt")
        self.button_takt.setIcon(icon_start)
        self.stop_takt_event.set()

    def start_takt(self):
       
        icon_stop = self.style().standardIcon(getattr(QStyle, "SP_MediaPause"))
        self.button_takt.setText("Stop Takt")
        self.button_takt.setIcon(icon_stop)
        bpm = self.line_edit_bpm.displayText()
        self.takt = Takt(int(bpm)) # line_edit_bpm is just expecting Ints, so no worryes.
        self.stop_takt_event= threading.Event()
        self.play_thread = threading.Thread(target=self.takt.play, args= [self.stop_takt_event])
        self.play_thread.start()