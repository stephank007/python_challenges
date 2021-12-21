#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Create a class with an insert method to insert an int to a list.  It should also support calculating the max, min, mean, and mode in O(1).
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
#     * No
# * Is there a range of inputs?
#     * 0 <= item <= 100
# * Should mean return a float?
#     * Yes
# * Should the other results return an int?
#     * Yes
# * If there are multiple modes, what do we return?
#     * Any of the modes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * [] -> ValueError
# * [5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
#     * max: 9
#     * min: 2
#     * mean: 55
#     * mode: 9 or 2

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def __init__(self, upper_limit=100):
        # TODO: Implement me
        pass

    def insert(self, val):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_math_ops.py
import unittest


class TestMathOps(unittest.TestCase):

    def test_math_ops(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.insert, None)
        solution.insert(5)
        solution.insert(2)
        solution.insert(7)
        solution.insert(9)
        solution.insert(9)
        solution.insert(2)
        solution.insert(9)
        solution.insert(4)
        solution.insert(3)
        solution.insert(3)
        solution.insert(2)
        self.assertEqual(solution.max, 9)
        self.assertEqual(solution.min, 2)
        self.assertEqual(solution.mean, 5)
        self.assertTrue(solution.mode in (2, 9))
        print('Success: test_math_ops')


def main():
    test = TestMathOps()
    test.test_math_ops()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
