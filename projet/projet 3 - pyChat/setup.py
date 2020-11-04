import sys
from cx_Freeze import setup, Executable
 

 
base = None
if sys.platform == "win32":
    base = "Win32GUI"
 
setup(
    name = "ProgrammeTkinter",
    version = "1.0",
    description = "Mon programme Tkinter",
    executables = [Executable("client.py", base = base)]
)