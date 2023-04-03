import subprocess, os

src_PATH="./src/"

try:
    f = open(src_PATH+"installed.md","r")
    f.close()

    # script da eseguire
    script_cmd = ['python', src_PATH+'RUN.py']

    # Esecuzione dello script
    os.system("python " +src_PATH+"RUN.py")
except:
    pass





