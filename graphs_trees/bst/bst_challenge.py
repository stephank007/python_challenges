#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

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
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst/bst_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Node(object):

    def __init__(self, data):
        # TODO: Implement me
        pass


class Bst(object):

    def insert(self, data):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


get_ipython().run_line_magic('run', 'dfs.py')


# In[ ]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[ ]:


# %load test_bst.py
import unittest


class TestTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__()
        self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst/bst_solution.ipynb) for a discussion on algorithms and code solutions.
