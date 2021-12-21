#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the highest product of three numbers in a list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the input a list of integers?
#     * Yes
# * Can we get negative inputs?
#     * Yes
# * Can there be duplicate entries in the input?
#     * Yes
# * Will there always be at least three integers?
#     * No
# * Can we assume the inputs are valid?
#     * No, check for None input
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * Less than three ints -> ValueError
# * [5, -2, 3] -> -30
# * [5, -2, 3, 1, -1, 4] -> 60

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def max_prod_three(self, array):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_prod_three.py
import unittest


class TestProdThree(unittest.TestCase):

    def test_prod_three(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.max_prod_three, None)
        self.assertRaises(ValueError, solution.max_prod_three, [1, 2])
        self.assertEqual(solution.max_prod_three([5, -2, 3]), -30)
        self.assertEqual(solution.max_prod_three([5, -2, 3, 1, -1, 4]), 60)
        print('Success: test_prod_three')


def main():
    test = TestProdThree()
    test.test_prod_three()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
