import cx_Freeze
from cx_Freeze import *

setup(
    name = 'Jarv',
    options = {'build_exe':{'packages': ['speech_recognition', 'pyttsx3', 'os', 'time', 'sys', 'webbrowser', 'datetime']}},
    executables = [
        Executable(
            'Jarv.py'
        )
    ]
)