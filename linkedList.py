class LinkedList:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.id=key
        self.data = value
        self.next = next
        self.prev = prev
        self.tail =self
        
    def __iter__(self):
        node=self
        while node.prev:
            yield (self.id,self.data)
            node=node.prev

    def __str__(self):
        s="["
        while self.prev:
            s+="("+str(self.id)+","+str(self.data)+")"+","
            self=self.prev
        s+=str(self.prev)
        s+="]"
        return s
 
    def append(self,key, value):
        
        node = self
        
        if node.next == None:
            node.next = LinkedList(key, value, None, node)
            self.tail=node.next
            return node.next
        else:
            return node.next.append(key,value)
    
    def find(self,key):
        node=self
        while node:
            if node.id == key:
                return node.data
            node = node.prev
            if node.prev == None:
                return None

    def remove(self,key):
        node=self
        while node.prev:
            if node.id == key:
                if node.next==None:
                    node.prev.next=None
                    node=node.prev
                    break

                elif node.prev==None:
                    node.next.prev=None
                    node = node.next
                    break
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node = node.next
                    break
            node=node.prev
    
                
