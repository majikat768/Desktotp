from PyQt6.QtWidgets import QApplication
import sys
from MainWindow import MainWindow
from resources import *
from DbHandler import table_exists, create_table

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

if __name__ == '__main__':
    if not table_exists():
        create_table()

    app = App(sys.argv)
    mainWindow = MainWindow()
    app.exec()



'''
other things:
pyotp can also generate urls ( otpauth://... ) which can translate into a qr code.
ergo, this app could store app secrets ( VERY UNSAFE ) which can then be retroactively used to transfer totp into a mobile app.
perhaps allow users to opt in to this.
also, this app's database should be encrypted for sure.
...
turns out sqlite doesn't support encryption.
alternative could be doing this in C++ instead.
'''