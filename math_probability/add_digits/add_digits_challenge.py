#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given an int, repeatedly add its digits until the result is one digit.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume num is not negative?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None input -> TypeError
# * negative input -> ValueError
# * 9 -> 9
# * 138 -> 3
# * 65536 -> 7
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def add_digits(self, val):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_add_digits.py
import unittest


class TestAddDigits(unittest.TestCase):

    def test_add_digits(self, func):
        self.assertRaises(TypeError, func, None)
        self.assertRaises(ValueError, func, -1)
        self.assertEqual(func(0), 0)
        self.assertEqual(func(9), 9)
        self.assertEqual(func(138), 3)
        self.assertEqual(func(65536), 7) 
        print('Success: test_add_digits')


def main():
    test = TestAddDigits()
    solution = Solution()
    test.test_add_digits(solution.add_digits)
    try:
        test.test_add_digits(solution.add_digits_optimized)
    except AttributeError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
