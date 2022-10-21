import sys
from PySide6 import QtCore, QtWidgets, QtGui 
from gui.window import Takt_Analyser_GUI
if __name__ == "__main__":
    app = QtWidgets.QApplication([])    

    widget = Takt_Analyser_GUI()
    
    widget.show()

    sys.exit(app.exec())
