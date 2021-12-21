#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given a list of stock prices, find the max profit from 1 buy and 1 sell.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Are all prices positive ints?
#     * Yes
# * Is the output an int?
#     * Yes
# * If profit is negative, do we return the smallest negative loss?
#     * Yes
# * If there are less than two prices, what do we return?
#     * Exception
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * Zero or one price -> ValueError
# * No profit
#     * [8, 5, 3, 2, 1] -> -1
# * General case
#     * [5, 3, 7, 4, 2, 6, 9] -> 7

# ## Algorithm
# 
# We'll use a greedy approach and iterate through the prices once.
# 
# * Loop through the prices
#     * Update current profit (price = min_price)
#     * Update the min price
#     * Update the max profit
# * Return max profit
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


import sys


class Solution(object):

    def find_max_profit(self, prices):
        if prices is None:
            raise TypeError('prices cannot be None')
        if len(prices) < 2:
            raise ValueError('prices must have at least two values')
        min_price = prices.pop(0)
        max_profit = prices[0] - min_price
        for price in prices:
            profit = price - min_price
            min_price = min(price, min_price)
            max_profit = max(profit, max_profit)
        return max_profit


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_max_profit.py', "import unittest\n\n\nclass TestMaxProfit(unittest.TestCase):\n\n    def test_max_profit(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.find_max_profit, None)\n        self.assertRaises(ValueError, solution.find_max_profit, [])\n        self.assertEqual(solution.find_max_profit([8, 5, 3, 2, 1]), -1)\n        self.assertEqual(solution.find_max_profit([5, 3, 7, 4, 2, 6, 9]), 7)\n        print('Success: test_max_profit')\n\n\ndef main():\n    test = TestMaxProfit()\n    test.test_max_profit()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_max_profit.py')

