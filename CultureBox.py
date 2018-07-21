from shuffler import Shuffler
from datastore import Datastore

class CultureBox:
	def __init__(self):
		self.datastore = Datastore("config.json")
		self.shuffler = Shuffler(self.datastore.get("insults"),
			self.datastore.get("compliments"))

if __name__ == "__main__":
	box = CultureBox()
	print(box.shuffler.randomInsults())