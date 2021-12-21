#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by Marco Guajardo. Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a binary search tree with insert, delete, different traversals & max/min node values
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# * Is this a binary tree?
#   * Yes
# * Is the root set to None initially?
#   * Yes
# * Do we care if the tree is balanced?
#   * No
# * What do we return for the traversals?
#   * Return a list of the data in the desired order
# * What type of data can the tree hold?
#   * Assume the tree only takes ints. In a realistic example, we'd use a hash table to convert other types to ints.

# ## Test Cases
# 
# ### Insert 
# 
# * Always start with the root
# * If value is less than the root, go to the left child
# * if value is more than the root, go to the right child
# 
# 
# ### Delete
# 
# * Deleting a node from a binary tree is tricky. Make sure you arrange the tree correctly when deleting a node.
# * Here are some basic [instructions](http://www.algolist.net/Data_structures/Binary_search_tree/Removal)
# * If the value to delete isn't on the tree return False
# 
# ### Traversals 
# 
# * In order traversal - left, center, right
# * Pre order traversal - center, left, right
# * Post order traversal - left, right, center
# * Return list for all traversals 
# 
# ### Max & Min
# * Find the max node in the binary search tree
# * Find the min node in the binary search tree
# 
# ### treeIsEmpty
# * check if the tree is empty
# 
# 
# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/binary_tree_implementation/binary_tree_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Node (object):
    def __init__ (self, data=None):
        #TODO:implement me
        pass
    
    def __str__ (self):
        #TODO:implement me
        pass


# In[ ]:


class BinaryTree (object):
    def __init__ (self):
        #TODO:implement me
        pass
    
    def insert (self, newData):
        #TODO:implement me
        pass
    
    def delete (self, key):
        #TODO:implement me
        pass
    
    def maxNode (self):
        #TODO:implement me
        pass
    
    def minNode (self):
        #TODO:implement me
        pass
    
    def printPostOrder (self):
        #TODO:implement me
        pass
    
    def printPreOrder (self):
        #TODO:implement me
        pass
    
    def printInOrder (self):
        #TODO:implement me
        pass
    
    def treeIsEmpty (self):
        #TODO: implement me
        pass


# ## Unit Test

# In[ ]:


import unittest

class TestBinaryTree(unittest.TestCase):

	def test_insert_traversals (self):
		myTree = BinaryTree()
		myTree2 = BinaryTree()
		for num in [50, 30, 70, 10, 40, 60, 80, 7, 25, 38]:
			myTree.insert(num)
		[myTree2.insert(num) for num in range (1, 100, 10)]

		print("Test: insert checking with in order traversal")
		expectVal = [7, 10, 25, 30, 38, 40, 50, 60, 70, 80]
		self.assertEqual(myTree.printInOrder(), expectVal)
		expectVal = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
		self.assertEqual(myTree2.printInOrder(), expectVal)

		print("Test: insert checking with post order traversal")
		expectVal = [7, 25, 10, 38, 40, 30, 60, 80, 70, 50]
		self.assertEqual(myTree.printPostOrder(), expectVal)
		expectVal = [91, 81, 71, 61, 51, 41, 31, 21, 11, 1]
		self.assertEqual(myTree2.printPostOrder(), expectVal)


		print("Test: insert checking with pre order traversal")
		expectVal = [50, 30, 10, 7, 25, 40, 38, 70, 60, 80]
		self.assertEqual(myTree.printPreOrder(), expectVal)
		expectVal = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
		self.assertEqual(myTree2.printPreOrder(), expectVal)


		print("Success: test_insert_traversals")

	def test_max_min_nodes (self):
		myTree = BinaryTree()
		myTree.insert(5)
		myTree.insert(1)
		myTree.insert(21)

		print("Test: max node")
		self.assertEqual(myTree.maxNode(), 21)
		myTree.insert(32)
		self.assertEqual(myTree.maxNode(), 32)

		print("Test: min node")
		self.assertEqual(myTree.minNode(), 1)

		print("Test: min node inserting negative number")
		myTree.insert(-10)
		self.assertEqual(myTree.minNode(), -10)

		print("Success: test_max_min_nodes")

	def test_delete (self):
		myTree = BinaryTree()
		myTree.insert(5)

		print("Test: delete")
		myTree.delete(5)
		self.assertEqual(myTree.treeIsEmpty(), True)
		
		print("Test: more complex deletions")
		[myTree.insert(x) for x in range(1, 5)]
		myTree.delete(2)
		self.assertEqual(myTree.root.rightChild.data, 3)
        
		print("Test: delete invalid value")
		self.assertEqual(myTree.delete(100), False)


		print("Success: test_delete")

def main():
    testing = TestBinaryTree()
    testing.test_insert_traversals()
    testing.test_max_min_nodes()
    testing.test_delete()
    
if __name__=='__main__':
    main()


# **The following unit test is expected to fail until you solve the challenge.**

# ## Solution NoteBook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/binary_tree_implementation/binary_tree_solution.ipynb) for a discussion on algorithms and code solutions.
