from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTreeWidget, QTreeWidgetItem
from AppList import AppList
from NewItemWindow import NewItemWindow
from resources import app_data_path
import os

class Body(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.appList = AppList(parent=self)
        self.layout.addWidget(self.appList)


        newAppBtn = QPushButton("Add new account")
        newAppBtn.clicked.connect(lambda : NewItemWindow(self))
        self.layout.addWidget(newAppBtn)

        appFolderBtn = QPushButton("app folder")
        appFolderBtn.clicked.connect(lambda : os.startfile(app_data_path))
        self.layout.addWidget(appFolderBtn)
        self.window().adjustSize()

    def getCurrentOtp(self):
        print(self.totp.now())