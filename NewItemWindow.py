from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget

class NewItemWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main = QWidget()
        self.main.layout = QVBoxLayout()
        self.main.setLayout(self.main.layout)

        self.appInputBox = QLineEdit()
        self.appInputBox.setPlaceholderText("enter app name")
        self.codeInputBox = QLineEdit()
        self.codeInputBox.setPlaceholderText("enter setup key")
        self.codeInputBtn = QPushButton("OK")
        self.codeInputBox.returnPressed.connect(self.submitSetupCode)
        self.codeInputBtn.clicked.connect(self.submitSetupCode)

        self.main.layout.addWidget(self.appInputBox)
        self.main.layout.addWidget(self.codeInputBox)
        self.main.layout.addWidget(self.codeInputBtn)

        self.setCentralWidget(self.main)
        self.show()

    def submitSetupCode(self):
        app = self.appInputBox.text()
        secret = self.codeInputBox.text()
        if len(app) <= 0 or len(secret) <= 0:
            return
        secret = secret.replace(' ','').upper()
        self.parent().appList.AddApp(app,secret)
        self.appInputBox.clear()
        self.codeInputBox.clear()
        self.close()
