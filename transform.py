def deflate(arrays):
	return [item for array in arrays for item in array]

def inflate(array,n):
	retlist=[]
	for i in xrange(0,len(array)-1,n):
		tmp = []
		for j in xrange(i,n+i,1):
			try:
				tmp.append(array[j])
			except IndexError:
				print "this is  j" + str(j)
				print len(array)
		retlist.append(tmp)
	return retlist 
	
