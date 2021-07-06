import ctypes
import time

#ouvre le lecteur 0
ctypes.windll.winmm.mciSendStringW("set cdaudio door open",None, 0, None)
time.sleep(3.5)
#et le ferme
ctypes.windll.winmm.mciSendStringW("set cdaudio door closed",None, 0, None)