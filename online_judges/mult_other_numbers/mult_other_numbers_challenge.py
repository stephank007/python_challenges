#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a list of ints, find the products of every other int for each index.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we use division?
#     * No
# * Is the output a list of ints?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> TypeError
# * [] -> []
# * [0] -> []
# * [0, 1] -> [1, 0]
# * [0, 1, 2] -> [2, 0, 0]
# * [1, 2, 3, 4] -> [24, 12, 8, 6]
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def mult_other_numbers(self, array):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_mult_other_numbers.py
import unittest


class TestMultOtherNumbers(unittest.TestCase):

    def test_mult_other_numbers(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.mult_other_numbers, None)
        self.assertEqual(solution.mult_other_numbers([0]), [])
        self.assertEqual(solution.mult_other_numbers([0, 1]), [1, 0])
        self.assertEqual(solution.mult_other_numbers([0, 1, 2]), [2, 0, 0])
        self.assertEqual(solution.mult_other_numbers([1, 2, 3, 4]), [24, 12, 8, 6])
        print('Success: test_mult_other_numbers')


def main():
    test = TestMultOtherNumbers()
    test.test_mult_other_numbers()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
