from linkedList import *
from collections import defaultdict

class hashtable:
	def __init__(self):
		self.buckets = [LinkedList() for i in range(30)]


	def _hash(self,key):
		return key % 30

	def insert(self, key, value):
		self.buckets[self._hash(key)].tail.append(key,value)

	def get(self,key):
		found = False
		s= "\nkey: "+str(key)
		s+="\nexpected bucket: "+str(self._hash(key))
		for bucket in self.buckets:
			
			if bucket.tail.find(key) != None:
				s+="\nFOUND\n\n"
				found=True
				s+="actual bucket: "+str(self.buckets.index(bucket))
				break
		if found ==False:
			s+="\nWTF!!!!\n"
			s+=str(self.buckets[self._hash(key)].tail)
		print s


	def remove(self, key):
		self.buckets[self._hash(key)].tail.remove(key)