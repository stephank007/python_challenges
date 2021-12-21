#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

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
# 
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
# * Loop through each character in the license key backwards, keeping a count of the number of chars we've reached so far, while inserting each character into a result list (convert to upper case)
#     * If we reach a '-', skip it
#     * Whenever we reach a char count of k, append a '-' character to the result list, reset the char count
# * Careful that we don't have a leading '-', which we might hit with test case: '2-4A0r7-4k', k=4 -> '24A0-R74K'
# * Reverse the result list and return it
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Code

# In[1]:


class Solution(object):

    def format_license_key(self, license_key, k):
        if license_key is None:
            raise TypeError('license_key must be a str')
        if not license_key:
            raise ValueError('license_key must not be empty')
        formatted_license_key = []
        num_chars = 0
        for char in license_key[::-1]:
            if char == '-':
                continue
            num_chars += 1
            formatted_license_key.append(char.upper())
            if num_chars >= k:
                formatted_license_key.append('-')
                num_chars = 0
        if formatted_license_key and formatted_license_key[-1] == '-':
            formatted_license_key.pop(-1)
        return ''.join(formatted_license_key[::-1])


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_format_license_key.py', "import unittest\n\n\nclass TestSolution(unittest.TestCase):\n\n    def test_format_license_key(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.format_license_key, None, None)\n        license_key = '---'\n        k = 3\n        expected = ''\n        self.assertEqual(solution.format_license_key(license_key, k), expected)\n        license_key = '2-4A0r7-4k'\n        k = 3\n        expected = '24-A0R-74K'\n        self.assertEqual(solution.format_license_key(license_key, k), expected)\n        license_key = '2-4A0r7-4k'\n        k = 4\n        expected = '24A0-R74K'\n        self.assertEqual(solution.format_license_key(license_key, k), expected)\n        print('Success: test_format_license_key')\n\ndef main():\n    test = TestSolution()\n    test.test_format_license_key()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_format_license_key.py')

