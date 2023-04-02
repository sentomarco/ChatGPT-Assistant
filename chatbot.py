import openai 

MAX_TOKEN = 4096

class ChatGPT():

	def __init__(self, key):

		#Define OpenAI API key 
		openai.api_key = key
		self.openai=openai
		#Set up the model and prompt 
		self.history = []

	#prompt = input('Enter new prompt: ') 
	
	def verify(self):
		try:
		    models = self.openai.Model.list()
		    return True
		except:
		    return False
	
	def Completion_model(self,prompt):
		model_engine = "text-davinci-003"
		# Generate a response
		completion = openai.Completion.create(
		    engine=model_engine,
		    prompt=prompt,
		    max_tokens=1024,
		    n=1,
		    stop=None,
		    temperature=0.5,
		)

		res = completion.choices[0].text
		return res

	
	def ChatCompletion_model(self,prompt):
		model_engine = "gpt-3.5-turbo"
		
		prompt_with_history = "\n".join(self.history + [prompt])
		# Generate a response
		
		if ( len( prompt_with_history.split(" ") ) > MAX_TOKEN*0.95): 
			i=-10
			
			while( ( len( prompt_with_history.split(" ") ) > MAX_TOKEN*0.5) or i!=-1):
			
				self.history=self.history[i:]
				prompt_with_history = "\n".join(self.history + [prompt])
				i+=1
		
		#defining the timeout:
		min_time = 20
		max_time = 40
		timeout = min_time + (max_time - min_time) * ( len( prompt_with_history.split(" ") ) / MAX_TOKEN ) 
		
		mex_struct = openai.ChatCompletion.create(
			model = model_engine, 
			messages =  [
				{"role": "user","content":prompt_with_history},
				],
			request_timeout=timeout
			) 
		res = mex_struct.choices[0]["message"]["content"].strip()
		return res
		
	
	#Generate a response 
	def response(self,prompt):
	
		self.history.append("You: " + prompt)
		res = self.ChatCompletion_model(prompt)
		self.history.append("ChatGPT: " + res)
		
		return res
		
		
		
		
		
		
		
		
		
		
