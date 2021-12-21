#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the second largest node in a binary search tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * If this is called on a None input or a single node, should we raise an exception?
#     * Yes
#         * None -> TypeError
#         * Single node -> ValueError
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None or single node -> Exception
# 
# <pre>
# Input:
#                 _10_
#               _/    \_          
#              5        15
#             / \       / \
#            3   8     12  20
#           /     \         \
#          2       4        30
# 
# Output: 20
# 
# Input:
#                  10
#                  /  
#                 5
#                / \
#               3   7
# Output: 7
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_second_largest/bst_second_largest_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class Solution(Bst):

    def find_second_largest(self):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_bst_second_largest.py
import unittest


class TestBstSecondLargest(unittest.TestCase):

    def test_bst_second_largest(self):
        bst = Solution(None)
        self.assertRaises(TypeError, bst.find_second_largest)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node15 = bst.insert(15)
        node3 = bst.insert(3)
        node8 = bst.insert(8)
        node12 = bst.insert(12)
        node20 = bst.insert(20)
        node2 = bst.insert(2)
        node4 = bst.insert(4)
        node30 = bst.insert(30)
        self.assertEqual(bst.find_second_largest(), node20)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node3 = bst.insert(3)
        node7 = bst.insert(7)
        self.assertEqual(bst.find_second_largest(), node7)
        print('Success: test_bst_second_largest')


def main():
    test = TestBstSecondLargest()
    test.test_bst_second_largest()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/check_balance/check_balance_solution.ipynb) for a discussion on algorithms and code solutions.
