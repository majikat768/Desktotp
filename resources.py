from PyQt6.QtCore import QStandardPaths, QSettings
import os, sys

app_data_path = os.path.join(QStandardPaths.writableLocation(
    QStandardPaths.StandardLocation.AppDataLocation),'desktotp')
if not os.path.exists(app_data_path):
    os.makedirs(app_data_path,exist_ok=True)


settings = QSettings(os.path.join(
    app_data_path, 'settings.ini'), QSettings.Format.IniFormat)

database = os.path.join(app_data_path, 'desktotp.db')

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


timeout = 30