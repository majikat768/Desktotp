from PyQt6.QtCore import QObject, pyqtSignal
import time
from resources import timeout

class Timer(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.appList = parent
        self.t = int(time.time()) % timeout

    def run(self):
        while True:
            time.sleep(1)
            self.progress.emit(self.t)
            self.t = (self.t+1) % timeout