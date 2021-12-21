#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the in-order successor of a given node in a binary search tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * If there is no successor, do we return None?
#     * Yes
# * If the input is None, should we throw an exception?
#     * Yes
# * Can we assume we already have a Node class that keeps track of parents?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
#           _5_
#         /     \
#        3       8
#       / \    /   \
#      2   4  6    12
#     /        \   / \
#    1          7 10  15
#                /
#               9
# 
# In: None  Out: Exception
# In: 4     Out: 5
# In: 5     Out: 6
# In: 8     Out: 9
# In: 15    Out: None
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_successor/bst_successor_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class BstSuccessor(object):

    def get_next(self, node):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_bst_successor.py
import unittest


class TestBstSuccessor(unittest.TestCase):

    def test_bst_successor_empty(self):
        bst_successor = BstSuccessor()
        bst_successor.get_next(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = Bst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)

        bst_successor = BstSuccessor()
        self.assertEqual(bst_successor.get_next(nodes[4]), 5)
        self.assertEqual(bst_successor.get_next(nodes[5]), 6)
        self.assertEqual(bst_successor.get_next(nodes[8]), 9)
        self.assertEqual(bst_successor.get_next(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.assertRaises(TypeError, test.test_bst_successor_empty)


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_successor/bst_successor_solution.ipynb) for a discussion on algorithms and code solutions.
