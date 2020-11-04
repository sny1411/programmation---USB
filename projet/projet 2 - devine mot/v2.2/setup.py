import sys
from cx_Freeze import setup, Executable
 
build_exe_options = {"includes": ["tkinter"]}
 
base = None
if sys.platform == "win32":
    base = "Win32GUI"
 
setup(
    name = "ProgrammeTkinter",
    version = "1.0",
    description = "Mon programme Tkinter",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base = base)]
)