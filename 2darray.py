def deflate(n_array):
	return [item for array in n_array for item in array]

def inflate(array,n,fillvalue=None):
	retlist=[]
	
	for i in xrange(0,len(array)-1,n):
		tmp = []
		for j in xrange(i,n+i,1):
			tmp.append(array[j])
		retlist.append(tmp)
	return retlist 
	
a = [[1,2,3],[4,5,6],[7,8,9]]
print len (a)

print inflate(deflate(a),len(a))