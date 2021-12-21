#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Format license keys.
# 
# See the [LeetCode](https://leetcode.com/problems/license-key-formatting/) problem page.
# 
# <pre>
# Now you are given a string S, which represents a software license key which we would like to format. The string S is composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string into groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are possibly misplaced.
# 
# We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all the lower case letters in the string must be converted to upper case.
# 
# So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to return the license key formatted according to the description above.
# 
# Example 1:
# Input: S = "2-4A0r7-4k", K = 4
# 
# Output: "24A0-R74K"
# 
# Explanation: The string S has been split into two parts, each part has 4 characters.
# Example 2:
# Input: S = "2-4A0r7-4k", K = 3
# 
# Output: "24-A0R-74K"
# 
# Explanation: The string S has been split into three parts, each part has 3 characters except the first part as it could be shorter as said above.
# Note:
# The length of string S will not exceed 12,000, and K is a positive integer.
# String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
# String S is non-empty.
# </pre>
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the output a string?
#     * Yes
# * Can we change the input string?
#     * No, you can't modify the input string
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * '---', k=3 -> ''
# * '2-4A0r7-4k', k=3 -> '24-A0R-74K'
# * '2-4A0r7-4k', k=4 -> '24A0-R74K'

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def format_license_key(self, license_key, k):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_format_license_key.py
import unittest


class TestSolution(unittest.TestCase):

    def test_format_license_key(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.format_license_key, None, None)
        license_key = '---'
        k = 3
        expected = ''
        self.assertEqual(solution.format_license_key(license_key, k), expected)
        license_key = '2-4A0r7-4k'
        k = 3
        expected = '24-A0R-74K'
        self.assertEqual(solution.format_license_key(license_key, k), expected)
        license_key = '2-4A0r7-4k'
        k = 4
        expected = '24A0-R74K'
        self.assertEqual(solution.format_license_key(license_key, k), expected)
        print('Success: test_format_license_key')

def main():
    test = TestSolution()
    test.test_format_license_key()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
