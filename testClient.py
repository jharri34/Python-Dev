from binaryTree import *
import random

def testClient():
	bt = binaryTree()
	val=[x for x in range(1,10,1)]
	root = bt.insert( val.pop(0))
	for i in val:
		print root.insert(i)

	root.preorder()

testClient()