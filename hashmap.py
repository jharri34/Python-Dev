class hashtable:
	def __init__(self, size):
		self.size = size
		self.keys = {}

	def hash(self,key):
		return key % self.size

	def insert(self, key, value):
		self.keys[hash(key)] = value
	
	def delete(self, key):
		if hash(key) in self.keys:
			del self.keys[hash(key)]
	
	def get(self,key):
		if hash(key) in self.keys:
			return self.keys[hash(key)]
