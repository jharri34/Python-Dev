content = []
def push(ele):
	content.append(ele)
	print content
	
def pop():
	print content
	return content.pop()

def enqueue(ele):
	push(ele)

def dequeue():
	print content
	return content.pop(0)



