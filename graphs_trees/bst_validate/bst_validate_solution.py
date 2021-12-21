#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine if a tree is a valid binary search tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can the tree have duplicates?
#     * Yes
# * If this is called on a None input, should we raise an exception?
#     * Yes
# * Can we assume we already have a Node class?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# None -> exception
# 
# <pre>
# Valid:
#       5
#     /   \
#    5     8
#   /     /
#  4     6
#         \
#          7
#         
# Invalid:
#       5
#     /   \
#    5     8
#     \   
#     20
# </pre>

# ## Algorithm
# 
# We'll use a recursive solution that validates left <= current < right, passing down the min and max values as we do a depth-first traversal.
# 
# * If the node is None, return True
# * If min is set and the node's value <= min, return False
# * if max is set and the node's value > max, return False
# * Recursively call the validate function on node.left, updating max
# * Recursively call the validate function on node.right, updating min
#     
# Complexity:
# * Time: O(n)
# * Space: O(h), where h is the height of the tree

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


import sys


class BstValidate(Bst):

    def validate(self):
        if self.root is None:
            raise TypeError('No root node')
        return self._validate(self.root)

    def _validate(self, node, minimum=-sys.maxsize, maximum=sys.maxsize):
        if node is None:
            return True
        if node.data <= minimum or node.data > maximum:
            return False
        if not self._validate(node.left, minimum, node.data):
            return False
        if not self._validate(node.right, node.data, maximum):
            return False
        return True


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_bst_validate.py', "import unittest\n\n\nclass TestBstValidate(unittest.TestCase):\n\n    def test_bst_validate_empty(self):\n        bst = BstValidate(None)\n        bst.validate()\n\n    def test_bst_validate(self):\n        bst = BstValidate(Node(5))\n        bst.insert(8)\n        bst.insert(5)\n        bst.insert(6)\n        bst.insert(4)\n        bst.insert(7)\n        self.assertEqual(bst.validate(), True)\n\n        bst = BstValidate(Node(5))\n        left = Node(5)\n        right = Node(8)\n        invalid = Node(20)\n        bst.root.left = left\n        bst.root.right = right\n        bst.root.left.right = invalid\n        self.assertEqual(bst.validate(), False)\n\n        print('Success: test_bst_validate')\n\n\ndef main():\n    test = TestBstValidate()\n    test.assertRaises(TypeError, test.test_bst_validate_empty)\n    test.test_bst_validate()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_bst_validate.py')

