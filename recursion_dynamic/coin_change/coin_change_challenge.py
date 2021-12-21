#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Determine the total number of unique ways to make n cents, given coins of denominations less than n cents.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Do the coins have to reach exactly n cents?
#     * Yes
# * Can we assume we have an infinite number of coins to make n cents?
#     * Yes
# * Do we need to report the combination(s) of coins that represent the minimum?
#     * No
# * Can we assume the coin denominations are given in sorted order?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * coins: None or n: None -> Exception
# * coins: [] or n: 0 -> 0
# * coins: [1, 2, 3], n: 5 -> 5

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/coin_change/coin_change_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class CoinChanger(object):

    def make_change(self, coins, total):
        # TODO: Implement me
        return n


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_coin_change.py
import unittest


class Challenge(unittest.TestCase):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        self.assertEqual(coin_changer.make_change([1, 2], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 5), 5)
        self.assertEqual(coin_changer.make_change([1, 5, 25, 50], 10), 3)
        print('Success: test_coin_change')


def main():
    test = Challenge()
    test.test_coin_change()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/coin_change/coin_change_solution.ipynb) for a discussion on algorithms and code solutions.
