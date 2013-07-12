from hashtable import *
from linkedList import *
import random

def testClient():
	ll=LinkedList()
	ht=hashtable()
	head = tail =ll
	keys = [x for x in range(256)]
	values = [int(1/random.random()) for _ in range(256)]

	for i in keys:
		ht.insert(keys[i],values[i])

	for i in range(50):
		key=random.choice(keys)
		ht.get(key)
		# print "real value is:"
		print "key: "+str(key)+" value: "+str(values[keys.index(key)])
	# for i in range(0,50,10):
	# 		tail = tail.append(keys[i],values[i])
	# node = head
	# print tail
testClient()