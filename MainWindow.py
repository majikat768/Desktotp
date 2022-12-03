from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTreeWidget, QTreeWidgetItem
from Body import Body
import pyotp, hashlib, base64

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.show()
        self.body = Body(self)
        self.setCentralWidget(self.body)
