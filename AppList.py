from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QPushButton, QSizePolicy, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import QThread
from PyQt6.QtGui import QPixmap,QImage
from Timer import Timer
from DbHandler import insert_row,get_accounts
import pyotp
from time import time
from resources import timeout
import qrcode
from PIL import ImageQt

class AppList(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderHidden(True)
        self.setColumnCount(3)
        self.init()
        self.startTimer()

    def startTimer(self):
        self.timer = Timer(self)
        thread = QThread(parent=self)
        self.timer.moveToThread(thread)
        thread.started.connect(self.timer.run)
        self.timer.finished.connect(thread.quit)
        self.timer.finished.connect(thread.deleteLater)
        self.timer.progress.connect(self.tick)
        thread.start()

    def init(self):
        accounts = get_accounts()
        for account in accounts:
            topItem = Item(account['account_name'],account['account_secret'])
            self.addTopLevelItem(topItem)
            topItem.initQr(self.parent())

    def tick(self,t):
        root = self.invisibleRootItem()
        item_count = root.childCount()
        for i in range(item_count):
            root.child(i).update(t)

    def AddApp(self,account_name,secret):
        row = {
            'account_name':account_name,
            'account_secret':secret,
            'creation_date':time()
        }
        insert_row(row)

        topItem = Item(account_name,secret)
        self.addTopLevelItem(topItem)
        topItem.initQr(self.parent())
        self.adjustSize()
        self.window().adjustSize()

class Item(QTreeWidgetItem):
    def __init__(self,name,secret):
        super().__init__()
        self.name = name
        self.setText(0,name)
        self.secretItem = QTreeWidgetItem()
        self.secretItem.secret = secret
        otp = pyotp.TOTP(self.secretItem.secret).now()
        otp = otp[:3] + ' ' + otp[3:]
        self.secretItem.setText(0,otp)
        self.addChild(self.secretItem)

    def update(self,t):
        if t % timeout == 0:
            otp = pyotp.TOTP(self.secretItem.secret).now()
            otp = otp[:3] + ' ' + otp[3:]
            self.secretItem.setText(0,otp)
        self.secretItem.setText(1,str(timeout-t))

    def initQr(self,parent):
        widget = QWidget()
        widget.layout = QVBoxLayout()
        widget.setLayout(widget.layout)
        uri = pyotp.TOTP(self.secretItem.secret).provisioning_uri(name=self.name,issuer_name="Desktotp")
        code = qrcode.make(uri)
        btn = QPushButton("QR Code")
        btn.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        btn.clicked.connect(lambda : QrWindow(code,parent=parent))
        widget.layout.addWidget(btn)
        self.treeWidget().setItemWidget(self.secretItem,2,widget)

class QrWindow(QMainWindow):
    def __init__(self, code, parent=None):
        super().__init__(parent)
        self.main = QWidget()
        self.main.layout = QVBoxLayout()
        self.main.setLayout(self.main.layout)
        self.setCentralWidget(self.main)
        img = ImageQt.ImageQt(code)
        self.label = QLabel()
        self.label.setPixmap(QPixmap.fromImage(img))
        self.main.layout.addWidget(self.label)
        self.show()
