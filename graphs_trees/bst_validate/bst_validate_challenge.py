#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Determine if a tree is a valid binary search tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

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
#   / \   /
#  4   9 7
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_validate/bst_validate_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class BstValidate(Bst):

    def validate(self):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_bst_validate.py
import unittest


class TestBstValidate(unittest.TestCase):

    def test_bst_validate_empty(self):
        bst = BstValidate(None)
        bst.validate()

    def test_bst_validate(self):
        bst = BstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        self.assertEqual(bst.validate(), True)

        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        self.assertEqual(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.assertRaises(TypeError, test.test_bst_validate_empty)
    test.test_bst_validate()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_validate/bst_validate_solution.ipynb) for a discussion on algorithms and code solutions.
