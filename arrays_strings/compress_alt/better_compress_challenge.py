#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [hashhar](https://github.com/hashhar). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BCCD4'.  Only compress the string if it saves space.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the string is ASCII?
#     * Yes
#     * Note: Unicode strings could require special handling depending on your language
# * Is this case sensitive?
#     * Yes
# * Can we use additional data structures?  
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * None -> None
# * '' -> ''
# * 'AABBCC' -> 'AABBCC'
# * 'AAABCCDDDD' -> 'A3BCCD4'

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/compress_alt/better_compress_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


def compress_string(string):
    # TODO: Implement me
    pass


# ## Unit Test

# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_compress.py
import unittest


class TestCompress(unittest.TestCase):

    def test_compress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDD'), 'A3BCCD4')
        self.assertEqual(
            func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'),
            'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3',
        )
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/compress_alt/better_compress_solution.ipynb) for a discussion on algorithms and code solutions.
