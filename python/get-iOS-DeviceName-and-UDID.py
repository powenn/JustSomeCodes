"""
Get iOS device name and its UDID then showing in console
supports multi devices connected
"""
import subprocess

IDEVICE_ID_EXEC = "idevice_id"
IDEVICE_NAME = "idevicename"

UDID = subprocess.check_output([IDEVICE_ID_EXEC, "-l"], stderr=subprocess.DEVNULL).decode().split("\n")

def get_udid_and_name() :
    info = str("")
    if UDID == [""]:
        info = "NO iOS Device connected"
    else:
        for udid in UDID[:-1] :
            DEVICENAME = subprocess.check_output([IDEVICE_NAME,"-u",f"{udid}"], stderr=subprocess.DEVNULL).decode().split("\n")
            for devicename in DEVICENAME[:-1]:
                info += f"iOS Device Name: {devicename}\nUDID: {udid}\n"
    print(info)

if __name__ == "__main__":
    get_udid_and_name()