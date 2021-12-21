#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Determine if a number is a power of two.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the input number an int?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Is the output a boolean?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * 0 -> False
# * 1 -> True
# * 2 -> True
# * 15 -> False
# * 16 -> True

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def is_power_of_two(self, val):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_is_power_of_two.py
import unittest


class TestSolution(unittest.TestCase):

    def test_is_power_of_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.is_power_of_two, None)
        self.assertEqual(solution.is_power_of_two(0), False)
        self.assertEqual(solution.is_power_of_two(1), True)
        self.assertEqual(solution.is_power_of_two(2), True)
        self.assertEqual(solution.is_power_of_two(15), False)
        self.assertEqual(solution.is_power_of_two(16), True)
        print('Success: test_is_power_of_two')


def main():
    test = TestSolution()
    test.test_is_power_of_two()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
