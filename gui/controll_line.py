
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QStyle, QLabel, QLineEdit
import threading
from backend.takt import Takt   
from backend.recorder import Recorder

class Controll_Line(QtWidgets.QHBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.create_takt_gui()
        self.create_recording_gui()
        self.create_analyser_gui()


    def create_recording_gui(self):
        self.is_recording = False
        icon_recording = self.parent.style().standardIcon(getattr(QStyle, "SP_DialogNoButton"))
        self.button_recording = QtWidgets.QPushButton(icon_recording, "")
        self.button_recording.clicked.connect(self.controll_recording)
        self.addWidget(self.button_recording)

    def create_takt_gui(self):
        # flag to decide which state GUI is 
        self.is_running_takt = False
        # start/stop - Button
        icon_play = self.parent.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
        self.button_takt = QtWidgets.QPushButton(icon_play, "")
        self.button_takt.clicked.connect(self.controll_takt)
        self.addWidget(self.button_takt)
        # bpm - Input
        self.line_edit_bpm = QLineEdit()
        self.line_edit_bpm.setText("120")
        onlyInt = QIntValidator()
        self.line_edit_bpm.setValidator(onlyInt)
        self.addWidget(self.line_edit_bpm)
        # bpm - Label
        self.text_bpm = QLabel("bpm")
        self.addWidget(self.text_bpm)

    def create_analyser_gui(self):
        self.is_analyser = False
        icon_play = self.parent.style().standardIcon(getattr(QStyle, "SP_FileDialogContentsView"))
        self.button_analyser = QtWidgets.QPushButton(icon_play, "")
        self.button_analyser.clicked.connect(self.controll_analyser)
        self.addWidget(self.button_analyser)

    @QtCore.Slot()
    def controll_takt(self):
        if (self.is_running_takt):
            self.is_running_takt = False
            icon_start = self.parent.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
            self.button_takt.setIcon(icon_start)
            self.button_analyser.setEnabled(True)
            self.stop_takt() 
        else:
            self.is_running_takt = True
            icon_stop = self.parent.style().standardIcon(getattr(QStyle, "SP_MediaPause"))
            self.button_takt.setIcon(icon_stop)
            self.button_analyser.setEnabled(False)
            self.start_takt()
   
    
    @QtCore.Slot()
    def controll_recording(self):
        if (self.is_recording):
            self.is_recording = False
            icon_start = self.parent.style().standardIcon(getattr(QStyle, "SP_DialogNoButton"))
            self.button_recording.setIcon(icon_start)
            self.button_analyser.setEnabled(True)
            self.stop_recording()
        else:
            self.is_recording = True
            icon_start = self.parent.style().standardIcon(getattr(QStyle, "SP_DialogSaveButton"))
            self.button_recording.setIcon(icon_start)
            self.button_analyser.setEnabled(False)
            self.start_recording()

    
    @QtCore.Slot()
    def controll_analyser(self):
        if (self.is_analyser):
            self.is_analyser = False
            icon_start = self.parent.style().standardIcon(getattr(QStyle, "SP_FileDialogContentsView"))
            self.button_analyser.setIcon(icon_start)
            self.button_takt.setEnabled(True)
            self.button_recording.setEnabled(True)
            self.stop_analyser()
        else:
            self.is_analyser = True
            icon_start = self.parent.style().standardIcon(getattr(QStyle, "SP_DialogSaveButton"))
            self.button_analyser.setIcon(icon_start)
            self.button_takt.setEnabled(False)
            self.button_recording.setEnabled(False)
            self.start_anaylser()
    
    def start_anaylser(self):
        self.start_takt()
        self.start_recording()

    def stop_analyser(self):
        self.stop_takt()
        self.stop_recording()
    
        
    def start_recording(self):
        recorder = Recorder()
        self.stop_recording_event= threading.Event()
        self.record_thread = threading.Thread(target=recorder.record, args= [self.stop_recording_event])
        self.record_thread.start()

    
    def stop_recording(self):
        self.stop_recording_event.set()
                 
    def stop_takt(self):
        self.stop_takt_event.set()

    def start_takt(self):
        bpm = self.line_edit_bpm.displayText()
        takt = Takt(int(bpm)) # line_edit_bpm is just expecting Ints, so no worryes.
        self.stop_takt_event= threading.Event()
        self.play_thread = threading.Thread(target=takt.play, args= [self.stop_takt_event])
        self.play_thread.start()
       