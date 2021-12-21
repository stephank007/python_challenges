#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Create a binary search tree with minimal height from a sorted array.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the array in increasing order?
#     * Yes
# * Are the array elements unique?
#     * Yes
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * 0, 1, 2, 3, 4, 5, 6 -> height 3
# * 0, 1, 2, 3, 4, 5, 6, 7 -> height 4

# ## Algorithm
# 
# To create a bst with minimum height, we need to use the middle element as the root.  We'll use recursion to divide the array in half and continue to pick the middle element from the left and right halves as the nodes to insert in the tree.
# 
# * create_min_bst(array, start, end)
# * Base case: Stop when end < start
# * Create a node with the mid element
# * Recursively build node.left by calling create_min_bst using the left sub array
# * Recursively build node.right by calling create_min_bst using the right sub array
# * Return the node
#     
# Complexity:
# * Time: O(n)
# * Space: O(h), where h is the tree's height (since this is a tree with minimum height, h = log n)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


from __future__ import division


class MinBst(object):

    def create_min_bst(self, array):
        if array is None:
            return
        return self._create_min_bst(array, 0, len(array) - 1)

    def _create_min_bst(self, array, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(array[mid])
        node.left = self._create_min_bst(array, start, mid - 1)
        node.right = self._create_min_bst(array, mid + 1, end)
        return node


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_bst_min.py', "import unittest\n\n\ndef height(node):\n    if node is None:\n        return 0\n    return 1 + max(height(node.left),\n                   height(node.right))\n\n\nclass TestBstMin(unittest.TestCase):\n\n    def test_bst_min(self):\n        min_bst = MinBst()\n        array = [0, 1, 2, 3, 4, 5, 6]\n        root = min_bst.create_min_bst(array)\n        self.assertEqual(height(root), 3)\n\n        min_bst = MinBst()\n        array = [0, 1, 2, 3, 4, 5, 6, 7]\n        root = min_bst.create_min_bst(array)\n        self.assertEqual(height(root), 4)\n\n        print('Success: test_bst_min')\n\n\ndef main():\n    test = TestBstMin()\n    test.test_bst_min()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_bst_min.py')

