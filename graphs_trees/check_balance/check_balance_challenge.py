#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Check if a binary tree is balanced.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is a balanced tree one where the heights of two sub trees of any node doesn't differ by more than 1?
#     * Yes
# * If this is called on a None input, should we raise an exception?
#     * Yes
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> No
# * 1 -> Yes
# * 5, 3, 8, 1, 4 -> Yes
# * 5, 3, 8, 9, 10 -> No

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/check_balance/check_balance_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class BstBalance(Bst):

    def check_balance(self):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_check_balance.py
import unittest


class TestCheckBalance(unittest.TestCase):

    def test_check_balance_empty(self):
        bst = BstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = BstBalance(Node(5))
        self.assertEqual(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        self.assertEqual(bst.check_balance(), True)

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        self.assertEqual(bst.check_balance(), False)

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        self.assertEqual(bst.check_balance(), True)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.assertRaises(TypeError, test.test_check_balance_empty)
    test.test_check_balance()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/check_balance/check_balance_solution.ipynb) for a discussion on algorithms and code solutions.
