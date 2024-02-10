import pystray
import pywintypes
import win32api
import win32con
import os
from PIL import Image #gives icon
from pystray import MenuItem as item
from win10toast import ToastNotifier

def onQuit():
    icon.visible = False
    icon.stop()

def set_res(height, width):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = height
    devmode.PelsHeight = width

    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    win32api.ChangeDisplaySettings(devmode,0)


if __name__ == '__main__':
    image = Image.open(r"C:\Users\mirsu\Desktop\Code\P\Projects\Scripts\ResChanger\icon.png")

    menu = (
        item("1920x1080", lambda: set_res(1920, 1080)),
        item("1280x960", lambda: set_res(1280,960)),
        item("Quit", onQuit)
    )
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()


