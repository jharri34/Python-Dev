from heapq import *

def heapsort(list):
	h = []
	for value in list:
		heappush(h,value)
	return [heappop(h) for i in range(len(h))]