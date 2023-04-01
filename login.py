import requests

def log(username, password):

	login_url = 'https://chat.openai.com/chat'
	csrf_token = 'csrftoken'

	# create a session object
	session = requests.session()

	# login data to be sent in the post request
	login_data = {
	    'csrfmiddlewaretoken': csrf_token,
	    'username': username,
	    'password': password
	}

	# send the post request to login
	response = session.post(login_url, data=login_data)

	# check if the login was successful
	if response.status_code == 200:
	    return True
	else:
	    return False
