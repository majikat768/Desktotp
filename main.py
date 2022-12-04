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