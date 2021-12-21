#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given two strings, find the longest common subsequence.
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
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class StringCompare(object):

    def longest_common_subseq(self, str0, str1):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_longest_common_subseq.py
import unittest


class TestLongestCommonSubseq(unittest.TestCase):

    def test_longest_common_subseq(self):
        str_comp = StringCompare()
        self.assertRaises(TypeError, str_comp.longest_common_subseq, None, None)
        self.assertEqual(str_comp.longest_common_subseq('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        self.assertEqual(str_comp.longest_common_subseq(str0, str1), expected)
        print('Success: test_longest_common_subseq')


def main():
    test = TestLongestCommonSubseq()
    test.test_longest_common_subseq()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
