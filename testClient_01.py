import random
import time
import heapsort
import quicksortIP
import quicksortOP

def testClient(testsize=100, *funcs):
	testpool = [random.sample(range(-32768,32767),x) for x in range(10, testsize, 10)]
	for func in funcs:
		while testpool > 0:
			print func(testpool.pop(0))

testClient(heapsort.heapsort, quicksortIP.quicksortIP, quicksortOP.quicksortOP)