import openai 


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
		mex_struct = openai.ChatCompletion.create(
			model = model_engine, 
			messages =  [
				{"role": "user","content":prompt_with_history},
				]
			) 
		res = mex_struct.choices[0]["message"]["content"].strip()
		return res
		
	
	#Generate a response 
	def response(self,prompt):
	
		self.history.append("You: " + prompt)
		res = self.ChatCompletion_model(prompt)
		self.history.append("ChatGPT: " + res)
		
		return res
		
		
		
		
		
		
		
		
		
		
