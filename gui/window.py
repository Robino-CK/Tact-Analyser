
from asyncio.windows_events import NULL
import imp
from PySide6 import  QtWidgets 
from gui.controll_line import Controll_Line
from gui.track_lines import Track_Lines
class Takt_Analyser_GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 50)
        self.setWindowTitle('Takt Analyser')
        self.layout = QtWidgets.QVBoxLayout(self)
        c_line = Controll_Line()
        self.layout.addLayout(c_line)
        t_lines = Track_Lines()        
        self.layout.addLayout(t_lines)
        