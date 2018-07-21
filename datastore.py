import json

class Datastore:

	def __init__(self, uri="config.json"):
		self.uri = uri
		self.store = {}
		self.refreshStore()

	def refreshStore(self):
		try:
			with open(self.uri, "r") as fh:
				self.store = json.loads(fh.read())
		except:
			pass
	
	def get(self, key):
		if key in self.store:
			return self.store[key]

	def set(self, key, value):
		self.store[key] = value
		with open(self.uri, "w") as fh:
			fh.write(json.dumps(self.store))

store = Datastore("config.json")
store.set("Hello", "test")