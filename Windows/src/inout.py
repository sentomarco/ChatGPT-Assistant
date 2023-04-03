import numpy as np
import speech_recognition as sr
import transformers, os
import sounddevice
from playsound import playsound
from gtts import gTTS
import colorTEXT as tx
from pydub import AudioSegment
from pydub.effects import speedup


def speed_audio(fileN, length):

	if length > 60: speed=1.5
	else: speed=1+0.5*length/60
	
	audio = AudioSegment.from_mp3(fileN)
	new_file = speedup(audio,1.5,150)
	new_file.export(fileN, format="mp3")


# Build the listener
class IO():

	def __init__(self, name="ChatGPT"):
		print("--- starting up", name, "---")
		self.name = name
		self.text = ""
		self.mic_index=len(sr.Microphone.list_microphone_names())-1 #AKA use the default microphone
		self.recognizer = sr.Recognizer()
		self.microphone = sr.Microphone(self.mic_index)
		self.humanL=""
		self.GPTL=""
		#print(sr.Microphone.list_microphone_names())
		
	def update_lang(self,human_lang, GPT_lang):
		self.humanL=human_lang
		self.GPTL=GPT_lang
		
		
	def speech_to_text(self):

		self.text = ""
		
		with  self.microphone as mic:
		    self.recognizer.adjust_for_ambient_noise(mic,duration=0.2)
		    print("\nlistening...\n")
		    
		    try:
		    	audio = self.recognizer.listen(mic, timeout=1)
		    except:
		    	self.text = -1
		    	
		if self.text!=-1:   
			try:
			    phrase = self.recognizer.recognize_google(audio, language =self.humanL, show_all=True)
			    self.text = phrase['alternative'][0]['transcript'].lower()
			    print(tx.OKBLUE, "😀 --> ", self.text, tx.ENDC)
			except:
			    self.text = -1
			    print(tx.WARNING, "* micrphone error *", tx.ENDC)
	    
	    
	def text_to_speech(self, text):
		print(tx.OKGREEN, "🤖 --> ", text, tx.ENDC)
		speaker = gTTS(text=text, lang=self.GPTL, slow=False)
		speaker.save("res.mp3")
		speed_audio("res.mp3", len(text.split(" ")) )
		playsound("res.mp3")
		#os.system("afplay res.mp3")  #mac->afplay | windows->start
		os.remove("res.mp3")

	#def wake_up(self, text):
        #	return True if self.name in text.lower() else False

