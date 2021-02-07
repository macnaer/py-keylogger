from cx_Freeze import setup, Executable

base = None

executables = [Executable("logger.py", base=base)]

packages = ["idna", "pynput", "threading", "smtplib", "time"]
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
    executables=executables
)