#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [mrb00l34n](http://github.com/mrb00l34n). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Counting Ways of Making Change.
# 
# * [Explanation](#Explanation)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Explanation
# 
# How many ways are there of making change for n, given an array of distinct coins? For example:
# 
# Input: n = 4, coins = [1, 2]
# 
# Output: 3. 1+1+1+1, 1+2+1, 2+2, would be the ways of making change.
# 
# Note that a coin can be used any number of times, and we are counting unique combinations.

# ## Test Cases
# 
# * Input: n = 0, coins = [1, 2] -> Output: 0
# * Input: n = 100, coins = [1, 2, 3] -> Output: 884
# * Input: n = 1000, coins = [1, 2, 3...99, 100] -> Output: 15658181104580771094597751280645
# 

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/coin_change_ways/coin_change_ways_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


def change_ways(n, coins):
    # TODO: Implement me
    return n


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_coin_change_ways.py
import unittest


class Challenge(unittest.TestCase):

    def test_coin_change_ways(self,solution):
        self.assertEqual(solution(0, [1, 2]), 0)
        self.assertEqual(solution(100, [1, 2, 3]), 884)
        self.assertEqual(solution(1000, range(1, 101)), 
                     15658181104580771094597751280645)
        print('Success: test_coin_change_ways')


def main():
    test = Challenge()
    test.test_coin_change_ways(change_ways)


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/coin_change_ways/coin_change_ways_solution.ipynb) for a discussion on algorithms and code solutions.
