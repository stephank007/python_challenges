#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the difference of two integers without using the + or - sign.
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
# <pre>
# * None input -> TypeError
# * 7, 5 -> 2
# * -5, -7 -> 2
# * -5, 7 -> -12
# * 5, -7 -> 12
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def sub_two(self, val):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_sub_two.py
import unittest


class TestSubTwo(unittest.TestCase):

    def test_sub_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.sub_two, None)
        self.assertEqual(solution.sub_two(7, 5), 2)
        self.assertEqual(solution.sub_two(-5, -7), 2)
        self.assertEqual(solution.sub_two(-5, 7), -12)
        self.assertEqual(solution.sub_two(5, -7), 12)
        print('Success: test_sub_two')


def main():
    test = TestSubTwo()
    test.test_sub_two()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
