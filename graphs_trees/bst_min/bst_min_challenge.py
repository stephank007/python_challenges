#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Create a binary search tree with minimal height from a sorted array.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

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
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_min/bst_min_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class MinBst(object):

    def create_min_bst(self, array):
    # TODO: Implement me


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_bst_min.py
import unittest


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),
                   height(node.right))


class TestBstMin(unittest.TestCase):

    def test_bst_min(self):
        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 3)

        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 4)

        print('Success: test_bst_min')


def main():
    test = TestBstMin()
    test.test_bst_min()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_min/bst_min_solution.ipynb) for a discussion on algorithms and code solutions.
