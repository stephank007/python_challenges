#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a list of stock prices, find the max profit from 1 buy and 1 sell.
# 
# See the [LeetCode](https://leetcode.com/problems/) problem page.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

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
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def find_max_profit(self, prices):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_max_profit.py
import unittest


class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_max_profit, None)
        self.assertRaises(ValueError, solution.find_max_profit, [])
        self.assertEqual(solution.find_max_profit([8, 5, 3, 2, 1]), -1)
        self.assertEqual(solution.find_max_profit([5, 3, 7, 4, 2, 6, 9]), 7)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
