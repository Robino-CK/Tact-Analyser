import sys
from PySide6 import QtCore, QtWidgets, QtGui 
from gui.window import MyWidget
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(200, 300)
    widget.show()

    sys.exit(app.exec())
