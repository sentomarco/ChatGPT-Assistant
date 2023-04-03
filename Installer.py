import subprocess, os


src_PATH="./src/"

try:
    f = open(src_PATH+"installed.md","r")
    f.close()
    
except:

    
    # lista delle librerie da installare
    libs_to_install = ['tk', 'openai', 'numpy', 'SpeechRecognition', 'playsound' , 'gTTS', 'pydub', 'transformers', 'sounddevice' ]
    os.system("clear")
    print("\n ********** Installing dependencies ********\n")

    pip_cmd = ['pip', 'install'] + libs_to_install
    # esecuzione del comando pip
    subprocess.Popen(pip_cmd)
    
    for pack in libs_to_install:
        os.system("pip install "+str(pack))
    
    #os.system(command)
    f = open(src_PATH+"installed.md","w")
    f.write("\n\nInstalled.\n\n")
    f.close()
   
    # esecuzione del comando "echo" con la stringa da stampare
    print("\n\n********** Done **********\n")


print("\n ********** Dependencies already satisfied. Execute chatGPTportable ********\n")

os.system("./chatGPTportable")
