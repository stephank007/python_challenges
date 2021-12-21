#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the Difference.
# 
# See the [LeetCode](https://leetcode.com/problems/find-the-difference/) problem page.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the strings are ASCII?
#     * Yes
# * Is case important?
#     * The strings are lower case
# * Can we assume the inputs are valid?
#     * No, check for None
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None input -> TypeError
# * 'aaabbcdd', 'abdbacade' -> 'e'

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def find_diff(self, s, t):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_str_diff.py
import unittest


class TestFindDiff(unittest.TestCase):

    def test_find_diff(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None)
        self.assertEqual(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
