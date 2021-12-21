#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given two strings, find the longest common subsequence.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume the inputs are valid?
#     * No
# * Can we assume the strings are ASCII?
#     * Yes
# * Is this case sensitive?
#     * Yes
# * Is a subsequence a non-contiguous block of chars?
#     * Yes
# * Do we expect a string as a result?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * str0 or str1 is None -> Exception
# * str0 or str1 equals 0 -> ''
# * General case
# 
# str0 = 'ABCDEFGHIJ'
# str1 = 'FOOBCDBCDE'
# 
# result: 'BCDE'

# ## Algorithm
# 
# We'll use bottom up dynamic programming to build a table.  
# 
# <pre>
# 
# The rows (i) represent str0.
# The columns (j) represent str1.
# 
#                        str1
#   -------------------------------------------------
#   |   |   | A | B | C | D | E | F | G | H | I | J |
#   -------------------------------------------------
#   |   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
#   | F | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
#   | O | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
# s | O | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
# t | B | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
# r | C | 0 | 0 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
# 0 | D | 0 | 0 | 1 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
#   | B | 0 | 0 | 1 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
#   | C | 0 | 0 | 1 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
#   | D | 0 | 0 | 1 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
#   | E | 0 | 0 | 1 | 2 | 3 | 4 | 4 | 4 | 4 | 4 | 4 |
#   -------------------------------------------------
# 
# if str1[j] != str0[i]:
#     T[i][j] = max(
#         T[i][j - 1],
#         T[i - 1][j])
# else:
#     T[i][j] = T[i - 1][j - 1] + 1
# </pre>
# 
# Complexity:
# * Time: O(m * n), where m is the length of str0 and n is the length of str1
# * Space: O(m * n), where m is the length of str0 and n is the length of str1

# ## Code

# In[1]:


class StringCompare(object):

    def longest_common_subseq(self, str0, str1):
        if str0 is None or str1 is None:
            raise TypeError('str input cannot be None')
        # Add one to number of rows and cols for the dp table's
        # first row of 0's and first col of 0's
        num_rows = len(str0) + 1
        num_cols = len(str1) + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                elif str0[j - 1] != str1[i - 1]:
                    T[i][j] = max(T[i][j - 1],
                                  T[i - 1][j])
                else:
                    T[i][j] = T[i - 1][j - 1] + 1
        results = ''
        i = num_rows - 1
        j = num_cols - 1
        # Walk backwards to determine the subsequence
        while T[i][j]:
            if T[i][j] == T[i][j - 1]:
                j -= 1
            elif T[i][j] == T[i - 1][j]:
                i -= 1
            elif T[i][j] == T[i - 1][j - 1] + 1:
                results += str1[i - 1]
                i -= 1
                j -= 1
            else:
                raise Exception('Error constructing table')
        # Walking backwards results in a string in reverse order
        return results[::-1]                


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_longest_common_subseq.py', "import unittest\n\n\nclass TestLongestCommonSubseq(unittest.TestCase):\n\n    def test_longest_common_subseq(self):\n        str_comp = StringCompare()\n        self.assertRaises(TypeError, str_comp.longest_common_subseq, None, None)\n        self.assertEqual(str_comp.longest_common_subseq('', ''), '')\n        str0 = 'ABCDEFGHIJ'\n        str1 = 'FOOBCDBCDE'\n        expected = 'BCDE'\n        self.assertEqual(str_comp.longest_common_subseq(str0, str1), expected)\n        print('Success: test_longest_common_subseq')\n\n\ndef main():\n    test = TestLongestCommonSubseq()\n    test.test_longest_common_subseq()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_longest_common_subseq.py')

