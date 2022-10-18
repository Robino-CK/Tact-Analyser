
from asyncio.windows_events import NULL
from PySide6 import  QtWidgets 
from gui.controll_line import Controll_Line

class Takt_Analyser_GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 50)
        self.setWindowTitle('Takt Analyser')
        self.layout = QtWidgets.QVBoxLayout(self)
        c_line = Controll_Line(self)
        self.layout.addLayout(c_line)
        
    