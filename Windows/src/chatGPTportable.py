import subprocess, os

src_PATH="./src/"


script_cmd = ['python', '.\src\RUN.py']

# Esecuzione dello script
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.Popen(script_cmd, startupinfo=startupinfo).wait()

    





