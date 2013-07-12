from linkedList import *
from collections import defaultdict

class hashtable:
	def __init__(self):
		self.buckets = [LinkedList() for i in range(30)]
	def _hash(self,key):
		return key % 30
	def insert(self, key, value):
		self.buckets[self._hash(key)].tail.append(key,value)
		# print "key: "+str(key)+" in bucket: "+str(self._hash(key)+" value: "+str(self.buckets[self._hash(key)].tail.find(key))
		#return self.buckets[self._hash(key)].tail.find(key)