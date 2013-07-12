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
	content.pop(0)

