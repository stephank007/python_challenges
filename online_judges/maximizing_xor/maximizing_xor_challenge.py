#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Maximizing XOR
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/maximizing-xor).
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/maximizing-xor).

# ## Test Cases
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/maximizing-xor).

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/hackerrank_topcoder/utopian_tree/maximizing_xor_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def max_xor(self, lower, upper):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_maximizing_xor.py
import unittest


class TestMaximizingXor(unittest.TestCase):

    def test_maximizing_xor(self):
        solution = Solution()
        self.assertEqual(solution.max_xor(10, 15), 7)
        print('Success: test_maximizing_xor')


def main():
    test = TestMaximizingXor()
    test.test_maximizing_xor()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/hackerrank_topcoder/utopian_tree/maximizing_xor_solution.ipynb) for a discussion on algorithms and code solutions.
