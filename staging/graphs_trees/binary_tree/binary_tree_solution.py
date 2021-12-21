#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by Marco Guajardo. Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

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

# ## Algorithm
# 
# ### Insert
# 
# * If root is none, insert at root
# * Else
#   * While node is not None
#       * if value is less go left child
#       * If value is more go right child
# 
# 
# * Time complexity: O(log(n))
# * Space complexity: O(n)
# 
# ### Min Node
# 
# * Keep going to the left child until you reach None and return the value
# 
# 
# * Time complexity: O(log(n))
# * Space complexity: O(n)
# 
# ### Max Node
# 
# * Keep going to the right child until you reach None and return the value
# 
# 
# * Time complexity: O(log(n))
# * Space complexity: O(n)
# 
# ### Traversals
# 
# * In order
#   * While the node is not None
#       * Call left child recursively
#       * Append data
#       * Call right child recursively 
#    
# * Post order
#   * While the node is not None
#       * Call left child recursively
#       * Call right child recursively 
#       * Append data
#  
# * Pre order
#   * While the node is not None
#       * Append data
#       * Call left child recursively
#       * Call right child recursively 
# 
# 
# * Time complexity: O(n) for all traversals
# * Space complexity: O(n)
# 
# ### Delete
# 
# * First, find value to delete
# * If value is not in tree 
#   * Return False
# * If value found
#   * Check if the node is a left child or right child
#     * If node is left child
#       * Find the biggest value in all the node's children and replace it with it
#     * If node is right child
#       * Find the smallest value in all the node's children and replace it with it
# 
# 
# * Time complexity: O(log(n))
# * Space complexity: O(n)
# 
# 

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'binary_search_tree.py', '\nclass Node (object):\n\tdef __init__ (self, data):\n\t\tself.data = data\n\t\tself.rightChild = None\n\t\tself.leftChild = None\n\nclass BinaryTree (object):\n\tdef __init__ (self):\n\t\tself.root = None\n\n\tdef insert (self, newData):\n\t\tleaf = Node(newData)\n\n\t\tif self.root is None:\n\t\t\tself.root = leaf\n\t\telse:\n\t\t\tcurrent = self.root\n\t\t\tparent = self.root\n\t\t\twhile current is not None:\n\t\t\t\tparent = current\n\t\t\t\tif newData < current.data:\n\t\t\t\t\tcurrent = current.leftChild\n\t\t\t\telse:\n\t\t\t\t\tcurrent = current.rightChild\n\n\t\t\tif newData < parent.data:\n\t\t\t\tparent.leftChild = leaf\n\t\t\telse:\n\t\t\t\tparent.rightChild = leaf\n\n\t# returns false if the item to be deleted is not on the tree\n\tdef delete (self, data):\n\t\tcurrent = self.root\n\t\tparent = self.root\n\t\tisLeft = False\n\n\t\tif current is None:\n\t\t\treturn False\n\n\t\twhile current is not None and current.data is not data:\n\t\t\tparent = current\n\t\t\tif data < current.data:\n\t\t\t\tcurrent = current.leftChild\n\t\t\t\tisLeft = True \n\t\t\telse:\n\t\t\t\tcurrent = current.rightChild\n\t\t\t\tisLeft = False\n\n\t\tif current is None:\n\t\t\treturn False\n\n\t\tif current.leftChild is None and current.rightChild is None:\n\t\t\tif current is self.root:\n\t\t\t\tself.root = None\n\t\t\telif isLeft:\n\t\t\t\tparent.leftChild = None\n\t\t\telse:\n\t\t\t\tparent.rightChild = None\n\n\t\telif current.rightChild is None:\n\t\t\tif current is self.root:\n\t\t\t\tself.root = current.leftChild\n\t\t\telif isLeft:\n\t\t\t\tparent.leftChild = current.leftChild\n\t\t\telse:\n\t\t\t\tparent.rightChild = current.leftChild\n\n\t\telif current.rightChild is None:\n\t\t\tif current is self.root:\n\t\t\t\tself.root = current.rightChild\n\t\t\telif isLeft:\n\t\t\t\tparent.lChild = current.rightChild\n\t\t\telse:\n\t\t\t\tparent.rightChild = current.rightChild\n\n\t\telse:\n\t\t\tsuccessor = current.rightChild\n\t\t\tsuccessorParent = current\n\n\t\t\twhile successor.leftChild is not None:\n\t\t\t\tsuccessorParent = successor\n\t\t\t\tsuccessor = successor.leftChild\n\n\t\t\tif current is self.root:\n\t\t\t\tself.root = successor\n\t\t\telif isLeft:\n\t\t\t\tparent.leftChild = successor\n\t\t\telse:\n\t\t\t\tparent.rightChild = successor\n\n\t\t\tsuccessor.leftChild = current.leftChild\n\n\t\t\tif successor is not current.rightChild:\n\t\t\t\tsuccessorParent.leftChild = successor.rightChild\n\t\t\t\tsuccessor.rightChild = current.rightChild\n\n\t\treturn True \n\n\n\tdef minNode (self):\n\t\tcurrent = self.root\n\t\twhile current.leftChild is not None:\n\t\t\tcurrent = current.leftChild\n\n\t\treturn current.data\n\n\tdef maxNode (self):\n\t\tcurrent = self.root\n\t\twhile current.rightChild is not None:\n\t\t\tcurrent = current.rightChild\n\n\t\treturn current.data\n\n\tdef printPostOrder (self):\n\t\tglobal postOrder\n\t\tpostOrder = []\n\n\t\tdef PostOrder(node):\n\t\t\tif node is not None:\n\t\t\t\tPostOrder(node.leftChild)\n\t\t\t\tPostOrder(node.rightChild)\n\t\t\t\tpostOrder.append(node.data)\n\n\t\tPostOrder(self.root)\n\t\treturn postOrder\n\n\tdef printInOrder (self):\n\t\tglobal inOrder \n\t\tinOrder = []\n\n\t\tdef InOrder (node):\n\t\t\tif node is not None:\n\t\t\t\tInOrder(node.leftChild)\n\t\t\t\tinOrder.append(node.data)\n\t\t\t\tInOrder(node.rightChild)\n\n\t\tInOrder(self.root)\n\t\treturn inOrder\n\n\tdef printPreOrder (self):\n\t\tglobal preOrder\n\t\tpreOrder = []\n\n\t\tdef PreOrder (node):\n\t\t\tif node is not None:\n\t\t\t\tpreOrder.append(node.data)\n\t\t\t\tPreOrder(node.leftChild)\n\t\t\t\tPreOrder(node.rightChild)\n\n\t\tPreOrder(self.root)\n\t\treturn preOrder\n\n\tdef treeIsEmpty (self):\n\t\treturn self.root is None')


# In[2]:


get_ipython().run_line_magic('run', 'binary_search_tree.py')


# In[3]:


get_ipython().run_cell_magic('writefile', 'test_binary_search_tree.py', 'import unittest\n\nclass TestBinaryTree(unittest.TestCase):\n\n\tdef test_insert_traversals (self):\n\t\tmyTree = BinaryTree()\n\t\tmyTree2 = BinaryTree()\n\t\tfor num in [50, 30, 70, 10, 40, 60, 80, 7, 25, 38]:\n\t\t\tmyTree.insert(num)\n\t\t[myTree2.insert(num) for num in range (1, 100, 10)]\n\n\t\tprint("Test: insert checking with in order traversal")\n\t\texpectVal = [7, 10, 25, 30, 38, 40, 50, 60, 70, 80]\n\t\tself.assertEqual(myTree.printInOrder(), expectVal)\n\t\texpectVal = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]\n\t\tself.assertEqual(myTree2.printInOrder(), expectVal)\n\n\t\tprint("Test: insert checking with post order traversal")\n\t\texpectVal = [7, 25, 10, 38, 40, 30, 60, 80, 70, 50]\n\t\tself.assertEqual(myTree.printPostOrder(), expectVal)\n\t\texpectVal = [91, 81, 71, 61, 51, 41, 31, 21, 11, 1]\n\t\tself.assertEqual(myTree2.printPostOrder(), expectVal)\n\n\n\t\tprint("Test: insert checking with pre order traversal")\n\t\texpectVal = [50, 30, 10, 7, 25, 40, 38, 70, 60, 80]\n\t\tself.assertEqual(myTree.printPreOrder(), expectVal)\n\t\texpectVal = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]\n\t\tself.assertEqual(myTree2.printPreOrder(), expectVal)\n\n\n\t\tprint("Success: test_insert_traversals")\n\n\tdef test_max_min_nodes (self):\n\t\tmyTree = BinaryTree()\n\t\tmyTree.insert(5)\n\t\tmyTree.insert(1)\n\t\tmyTree.insert(21)\n\n\t\tprint("Test: max node")\n\t\tself.assertEqual(myTree.maxNode(), 21)\n\t\tmyTree.insert(32)\n\t\tself.assertEqual(myTree.maxNode(), 32)\n\n\t\tprint("Test: min node")\n\t\tself.assertEqual(myTree.minNode(), 1)\n\n\t\tprint("Test: min node inserting negative number")\n\t\tmyTree.insert(-10)\n\t\tself.assertEqual(myTree.minNode(), -10)\n\n\t\tprint("Success: test_max_min_nodes")\n\n\tdef test_delete (self):\n\t\tmyTree = BinaryTree()\n\t\tmyTree.insert(5)\n\n\t\tprint("Test: delete")\n\t\tmyTree.delete(5)\n\t\tself.assertEqual(myTree.treeIsEmpty(), True)\n\t\t\n\t\tprint("Test: more complex deletions")\n\t\t[myTree.insert(x) for x in range(1, 5)]\n\t\tmyTree.delete(2)\n\t\tself.assertEqual(myTree.root.rightChild.data, 3)\n        \n\t\tprint("Test: delete invalid value")\n\t\tself.assertEqual(myTree.delete(100), False)\n\n\n\t\tprint("Success: test_delete")\n\ndef main():\n    testing = TestBinaryTree()\n    testing.test_insert_traversals()\n    testing.test_max_min_nodes()\n    testing.test_delete()\n    \nif __name__==\'__main__\':\n    main()')


# In[4]:


get_ipython().run_line_magic('run', '-i test_binary_search_tree.py')

