
from asyncio.windows_events import NULL
from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QLabel, QLineEdit
import threading
from backend.takt import Takt   
from backend.recorder import Recorder

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 50)
        self.setWindowTitle('Takt Analyser')
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(self.get_controlling_line())
        
    def get_controlling_line(self):
        hline = QtWidgets.QHBoxLayout()
        self.create_takt_gui(hline)
        self.create_recording_gui(hline)
        return hline

    def create_recording_gui(self, line):
        self.is_recording = False
        icon_recording = self.style().standardIcon(getattr(QStyle, "SP_DialogNoButton"))
        self.button_recording = QtWidgets.QPushButton(icon_recording, "")
        self.button_recording.clicked.connect(self.controll_recording)
        line.addWidget(self.button_recording)

    def create_takt_gui(self, line):
        # flag to decide which state GUI is 
        self.is_running_takt = False
        # start/stop - Button
        icon_play = self.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
        self.button_takt = QtWidgets.QPushButton(icon_play, "")
        self.button_takt.clicked.connect(self.controll_takt)
        line.addWidget(self.button_takt)
        # bpm - Input
        self.line_edit_bpm = QLineEdit()
        self.line_edit_bpm.setText("120")
        onlyInt = QIntValidator()
        self.line_edit_bpm.setValidator(onlyInt)
        line.addWidget(self.line_edit_bpm)
        # bpm - Label
        self.text_bpm = QLabel("bpm")
        line.addWidget(self.text_bpm)

        

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
        self.button_takt.setIcon(icon_start)
        self.stop_takt_event.set()

    def start_takt(self):
        icon_stop = self.style().standardIcon(getattr(QStyle, "SP_MediaPause"))
        self.button_takt.setIcon(icon_stop)
        bpm = self.line_edit_bpm.displayText()
        takt = Takt(int(bpm)) # line_edit_bpm is just expecting Ints, so no worryes.
        self.stop_takt_event= threading.Event()
        self.play_thread = threading.Thread(target=takt.play, args= [self.stop_takt_event])
        self.play_thread.start()

    @QtCore.Slot()
    def controll_recording(self):
        if (self.is_recording):
            self.is_recording = False
            self.stop_recording()
        else:
            self.is_recording = True
            self.start_recording()
    
    def start_recording(self):
        icon_start = self.style().standardIcon(getattr(QStyle, "SP_DialogSaveButton"))
        self.button_recording.setIcon(icon_start)
        recorder = Recorder()
        self.stop_recording_event= threading.Event()
        self.record_thread = threading.Thread(target=recorder.record, args= [self.stop_recording_event])
        self.record_thread.start()

    
    def stop_recording(self):
        icon_start = self.style().standardIcon(getattr(QStyle, "SP_DialogNoButton"))
        self.button_recording.setIcon(icon_start)
        self.stop_recording_event.set()