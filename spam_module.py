import requests

# Spam module
class SpamModule:
	#region Constructors etc
	def __init__(self, endpoint, apikey = ""):
		self.endpoint = endpoint
		self.apikey = apikey
		self.message_id = 0

	def __repr__(self) -> str:
		return f"{type(self).__name__} (endpoint={self.endpoint})"
	#endregion Constructors etc



	def spam(self, email, pwd):
		# Construct data to send to the endpoint
		data = {
			'api_dev_key': self.apikey,
			'email': email,
			'password': pwd,
		}

		# Post request
		self.message_id = self.message_id + 1
		message_id = self.message_id
		print(f"POST Message #{message_id} – email: \"{email}\"; pwd: \"{pwd}\"")
		r = requests.post(url = self.endpoint, data = data)
		print(f"RESPONSE Message #{message_id} STATUS {r.status_code} – time taken: {r.elapsed}")


