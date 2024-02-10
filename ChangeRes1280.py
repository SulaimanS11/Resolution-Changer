import pywintypes
import win32api
import win32con

devmode = pywintypes.DEVMODEType()
devmode.PelsWidth = 1280
devmode.PelsHeight = 960

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

def main():
    win32api.ChangeDisplaySettings(devmode,0)