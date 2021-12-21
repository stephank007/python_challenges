#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the sum of two integers without using the + or - sign.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the inputs are valid?
#     * No, check for None
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# See the [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) problem page.

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def sum_two(self, val):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_sum_two.py
import unittest


class TestSumTwo(unittest.TestCase):

    def test_sum_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.sum_two, None)
        self.assertEqual(solution.sum_two(5, 7), 12)
        self.assertEqual(solution.sum_two(-5, -7), -12)
        self.assertEqual(solution.sum_two(5, -7), -2)
        print('Success: test_sum_two')


def main():
    test = TestSumTwo()
    test.test_sum_two()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
