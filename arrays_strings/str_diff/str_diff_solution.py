#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the single different char between two strings.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume the strings are ASCII?
#     * Yes
# * Is case important?
#     * The strings are lower case
# * Can we assume the inputs are valid?
#     * No, check for None
#     * Otherwise, assume there is only a single different char between the two strings
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None input -> TypeError
# * 'ab', 'aab' -> 'a'
# * 'aab', 'ab' -> 'a'
# * 'abcd', 'abcde' -> 'e'
# * 'aaabbcdd', 'abdbacade' -> 'e'

# ## Algorithm
# 
# ### Dictionary
# 
# * Keep a dictionary of seen values in s
# * Loop through t, decrementing the seen values
#     * If the char is not there or if the decrement results in a negative value, return the char
# * Return the differing char from the dictionary
# 
# Complexity:
# * Time: O(m+n), where m and n are the lengths of s, t
# * Space: O(h), for the dict, where h is the unique chars in s
# 
# ### XOR
# 
# * XOR the two strings, which will isolate the differing char
# 
# Complexity:
# * Time: O(m+n), where m and n are the lengths of s, t
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')
        seen = {}
        for char in str1:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        for char in str2:
            try:
                seen[char] -= 1
            except KeyError:
                return char
            if seen[char] < 0:
                return char
        for char, count in seen.items():
            return char

    def find_diff_xor(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')
        result = 0
        for char in str1:
            result ^= ord(char)
        for char in str2:
            result ^= ord(char)
        return chr(result)


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_str_diff.py', "import unittest\n\n\nclass TestFindDiff(unittest.TestCase):\n\n    def test_find_diff(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.find_diff, None)\n        self.assertEqual(solution.find_diff('ab', 'aab'), 'a')\n        self.assertEqual(solution.find_diff('aab', 'ab'), 'a')\n        self.assertEqual(solution.find_diff('abcd', 'abcde'), 'e')\n        self.assertEqual(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')\n        self.assertEqual(solution.find_diff_xor('ab', 'aab'), 'a')\n        self.assertEqual(solution.find_diff_xor('aab', 'ab'), 'a')\n        self.assertEqual(solution.find_diff_xor('abcd', 'abcde'), 'e')\n        self.assertEqual(solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')\n        print('Success: test_find_diff')\n\n\ndef main():\n    test = TestFindDiff()\n    test.test_find_diff()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_str_diff.py')

