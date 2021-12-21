#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine the height of a tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is this a binary tree?
#     * Yes
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * 5 -> 1
# * 5, 2, 8, 1, 3 -> 3

# ## Algorithm
# 
# We'll use a recursive algorithm.
# 
# * If the current node is None, return 0
# * Else, return 1 + the maximum height of the left or right children
#     
# Complexity:
# * Time: O(n)
# * Space: O(h), where h is the height of the tree

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


class BstHeight(Bst):

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left),
                       self.height(node.right))


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_height.py', "import unittest\n\n\nclass TestHeight(unittest.TestCase):\n\n    def test_height(self):\n        bst = BstHeight(Node(5))\n        self.assertEqual(bst.height(bst.root), 1)\n        bst.insert(2)\n        bst.insert(8)\n        bst.insert(1)\n        bst.insert(3)\n        self.assertEqual(bst.height(bst.root), 3)\n\n        print('Success: test_height')\n\n\ndef main():\n    test = TestHeight()\n    test.test_height()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_height.py')

