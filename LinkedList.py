<<ListNode>>=
	class ListNode:
		def __init__(self,data,next,last):
			self.data=data
			self.next=next
			self.last=last
	<<List class>>=
    	def insert(self, node, data):
        	new_node = ListNode(data, node.next)
        	node.next = new_node
        	if self.tail == node:
            	self.tail = new_node
	<<List class >>=
		class List:
			def __init__(self):
				self.head = None
				self.tail = None
			def insert_end(self,data):
				if self.tail is None:
					new_node =  ListNode(data,None)
					self.head = self.tail = new_node
node3 = ListNode(3,None,node2)
node2 = ListNode(2,node3,node)
node  = ListNode(1,node2,None) 