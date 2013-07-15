class BSTnode(object):

    def __init__(self, t):
        """Create a new leaf with key t."""
        self.key = t
        self.disconnect()
    def disconnect(self):
        """sets all of the node references to None"""
        self.left = None
        self.right = None
        self.parent = None

class BST(object):
    """init root to None only called once"""
    def __init__(self):
        self.root = None

    def insert(self, t):
        """Insert key t into this BST, modifying it in-place."""
        new = BSTnode(t) #defines a new node in the binary tree
        if self.root is None:   #sets the root node
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:
                    # Go left
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break 
                    node = node.left
                else:
                    # Go right
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

     def find(self, t):
        """Return the node for key t if it is in this tree, or None otherwise."""
        if t == self.key:
            return self
        elif t < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(t)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(t)

    def delete(self):
        """"Delete this node from the tree."""
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent 
            current = self.parent
            while current.key is not None:
                current.update_stats()
                current = current.parent
            return self
        else:
            s = self.successor()
            self.key, s.key = s.key, self.key
            return s.delete()   

    def inorder(self):
        self.left.inorder()
        #visit
        self.right.inorder()

    def preorder(self):
        #visit
        self.left.inorder()
        self.right.inorder()

    def postorder(self):
        self.left.inorder()
        self.right.inorder()
        #visit

        pass
    def find(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = self.root
        while node is not None:
            if t == node.key:
                return node
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return None


    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])



def test(args=None, BSTtype=BST):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print 'usage: %s <number-of-random-items | item item item ...>' % \
              sys.argv[0]
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in xrange(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print tree
    for item in items:
        tree.insert(item)
        print
        print tree

if __name__ == '__main__': test()
