#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Utopian Tree
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/utopian-tree).
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/utopian-tree).

# ## Test Cases
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/utopian-tree).

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/hackerrank_topcoder/utopian_tree/utopian_tree_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def calc_utopian_tree_height(self, cycles):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_utopian_tree.py
import unittest


class TestUtopianTree(unittest.TestCase):

    def test_utopian_tree(self):
        solution = Solution()
        self.assertEqual(solution.calc_utopian_tree_height(0), 1)
        self.assertEqual(solution.calc_utopian_tree_height(1), 2)
        self.assertEqual(solution.calc_utopian_tree_height(4), 7)
        print('Success: test_utopian_tree')


def main():
    test = TestUtopianTree()
    test.test_utopian_tree()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/hackerrank_topcoder/utopian_tree/utopian_tree_solution.ipynb) for a discussion on algorithms and code solutions.
