#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a binary search tree with an insert method.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we insert None values?
#     * No
# * Can we assume we are working with valid integers?
#     * Yes
# * Can we assume all left descendents <= n < all right descendents?
#     * Yes
# * Do we have to keep track of the parent nodes?
#     * This is optional
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# ### Insert
# 
# Insert will be tested through the following traversal:
# 
# ### In-Order Traversal
# 
# * 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
# * 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
# 
# If the `root` input is `None`, return a tree with the only element being the new root node.
# 
# You do not have to code the in-order traversal, it is part of the unit test.

# ## Algorithm
# 
# ### Insert
# 
# * If the root is None, return Node(data)
# * If the data is <= the current node's data
#     * If the current node's left child is None, set it to Node(data)
#     * Else, recursively call insert on the left child
# * Else
#     * If the current node's right child is None, set it to Node(data)
#     * Else, recursively call insert on the right child
# 
# Complexity:
# 
# * Time: O(h), where h is the height of the tree
#     * In a balanced tree, the height is O(log(n))
#     * In the worst case we have a linked list structure with O(n)
# * Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'bst.py', "class Node(object):\n\n    def __init__(self, data):\n        self.data = data\n        self.left = None\n        self.right = None\n        self.parent = None\n\n    def __repr__(self):\n        return str(self.data)\n\n\nclass Bst(object):\n\n    def __init__(self, root=None):\n        self.root = root\n\n    def insert(self, data):\n        if data is None:\n            raise TypeError('data cannot be None')\n        if self.root is None:\n            self.root = Node(data)\n            return self.root\n        else:\n            return self._insert(self.root, data)\n\n    def _insert(self, node, data):\n        if node is None:\n            return Node(data)\n        if data <= node.data:\n            if node.left is None:\n                node.left = self._insert(node.left, data)\n                node.left.parent = node\n                return node.left\n            else:\n                return self._insert(node.left, data)\n        else:\n            if node.right is None:\n                node.right = self._insert(node.right, data)\n                node.right.parent = node\n                return node.right\n            else:\n                return self._insert(node.right, data)")


# In[2]:


get_ipython().run_line_magic('run', 'bst.py')


# ## Unit Test

# In[3]:


get_ipython().run_line_magic('run', 'dfs.py')


# In[4]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[5]:


get_ipython().run_cell_magic('writefile', 'test_bst.py', "import unittest\n\n\nclass TestTree(unittest.TestCase):\n\n    def __init__(self, *args, **kwargs):\n        super(TestTree, self).__init__()\n        self.results = Results()\n\n    def test_tree_one(self):\n        bst = Bst()\n        bst.insert(5)\n        bst.insert(2)\n        bst.insert(8)\n        bst.insert(1)\n        bst.insert(3)\n        in_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), '[1, 2, 3, 5, 8]')\n        self.results.clear_results()\n\n    def test_tree_two(self):\n        bst = Bst()\n        bst.insert(1)\n        bst.insert(2)\n        bst.insert(3)\n        bst.insert(4)\n        bst.insert(5)\n        in_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), '[1, 2, 3, 4, 5]')\n\n        print('Success: test_tree')\n\n\ndef main():\n    test = TestTree()\n    test.test_tree_one()\n    test.test_tree_two()\n\n\nif __name__ == '__main__':\n    main()")


# In[6]:


get_ipython().run_line_magic('run', '-i test_bst.py')

