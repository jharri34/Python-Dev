class binaryTree(object):
    def __init__(self=None, value=None, leftchild=None, rightchild=None, 
                 parent=None, root=False):
        self.value = value
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.parent = parent
        self.root = root


    def insert(self, value):
        if self is None:
            self = binaryTree(value, None, None, None, True)
            return self
        if self.leftchild is None and self.value >= value:
            self.leftchild = binaryTree(value,None,None,self)
            return self.leftchild
        if self.rightchild is None and self.value < value:
            self.rightchild = binaryTree(value,None,None,self)
            return self.rightchild
        self.leftchild.insert(value)
        self.rightchild.insert(value)

    def preorder(self):
        self = self
        print self.value
        if self.leftchild:
            print self.leftchild
            self.leftchild.preorder()
        print "failed first if"
        if self. rightchild:
            print self.rightchild
            self.rightchild.preorder()
        print "failed second if"

    def inorder(self):
        self = self
        if self is not None:
            print self.value
            
        if self.leftchild is not None:
            self.leftchild.inorder()
        if self.rightchild is not None:
            self.rightchild.inorder()
