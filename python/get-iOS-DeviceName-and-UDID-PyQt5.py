"""
Get iOS device name and its UDID then showing with PyQT5 message box 
supports multi devices connected
"""
import subprocess
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

IDEVICE_ID_EXEC = "idevice_id"
IDEVICE_NAME = "idevicename"

UDID = subprocess.check_output([IDEVICE_ID_EXEC, "-l"], stderr=subprocess.DEVNULL).decode().split("\n")
GUI_APPLICATION = QApplication(sys.argv)

def get_udid_and_name() :
    info = str("")
    if UDID == [""]:
        info = "NO iOS Device connected"
    else:
        for udid in UDID[:-1] :
            try:
                DEVICENAME = subprocess.check_output([IDEVICE_NAME,"-u",f"{udid}"], stderr=subprocess.DEVNULL).decode().split("\n")
                for devicename in DEVICENAME[:-1]:
                    info += f"iOS Device Name: {devicename}\nUDID: {udid}\n"
            except subprocess.CalledProcessError:
                info = (
                "Please make sure your iOS device is connected\n"
                "You may need to accept the trust dialog\n"
                "on your device before trying again"
                )

    # print(info)
    return info

def gui_initialization():
    # Initialize QT application
    GUI_APPLICATION.setQuitOnLastWindowClosed(False)

    device_info_box = QMessageBox()
    device_info_box.setText(get_udid_and_name())
    device_info_box.setFont(QFont("", 12))
    device_info_box.exec()

    GUI_APPLICATION.quit()

if __name__ == "__main__":
    # Start GUI
    gui_initialization()