
from asyncio.windows_events import NULL
from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget
import threading
from backend.takt import Takt   

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.recording = False
        icon_play = self.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
        self.button_takt = QtWidgets.QPushButton(icon_play, "Start Takt")
        self.button_record = QtWidgets.QPushButton("Click me3!")
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.button_takt)

        self.button_takt.clicked.connect(self.controll_takt)

    @QtCore.Slot()
    def controll_takt(self):
        if (self.recording):
            self.recording = False
            icon_start = self.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
            self.button_takt.setText("Start Takt")
            self.button_takt.setIcon(icon_start)
            self.stop_event.set()
        else:
            self.recording = True
            icon_stop = self.style().standardIcon(getattr(QStyle, "SP_MediaPause"))
            self.button_takt.setText("Stop Takt")
            self.button_takt.setIcon(icon_stop)
            self.takt = Takt(120)
            self.stop_event= threading.Event()
            self.play_thread = threading.Thread(target=self.takt.play, args= [self.stop_event])
            self.play_thread.start()
        
