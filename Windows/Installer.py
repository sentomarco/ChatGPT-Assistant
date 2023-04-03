import subprocess, os


src_PATH=".\\src\\"

    
# lista delle librerie da installare
libs_to_install = ['tk', 'openai', 'numpy', 'SpeechRecognition', 'playsound' , 'gTTS', 'pydub', 'transformers', 'sounddevice', 'pyinstaller']
os.system("clear")
print("\n ********** Please make sure to have Python installed ********\n")
print("\n ********** Installing dependencies ********\n")

pip_cmd = ['pip', 'install'] + libs_to_install
# esecuzione del comando pip
subprocess.Popen(pip_cmd)

for pack in libs_to_install:
	os.system("pip install "+str(pack))

os.system("python -m PyInstaller --onefile --noconsole --icon=chat.ico --distpath . .\\src\\chatGPTportable.py")
#os.system("move .\chatGPTportable\chatGPTportable.exe . ")


# esecuzione del comando "echo" con la stringa da stampare
print("\n\n********** Done **********\n")

