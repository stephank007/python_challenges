#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a positive integer, get the next largest number and the next smallest number with the same number of 1's as the given number.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the output a positive int?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * 0 -> Exception
# * negative int -> Exception
# * General case:
# <pre>
#     * Input:         0000 0000 1101 0111
#     * Next largest:  0000 0000 1101 1011
#     * Next smallest: 0000 0000 1100 1111
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Bits(object):

    def get_next_largest(self, num):
        # TODO: Implement me
        pass

    def get_next_smallest(self, num):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_get_next_largest.py
import unittest


class TestBits(unittest.TestCase):

    def test_get_next_largest(self):
        bits = Bits()
        self.assertRaises(Exception, bits.get_next_largest, None)
        self.assertRaises(Exception, bits.get_next_largest, 0)
        self.assertRaises(Exception, bits.get_next_largest, -1)
        num = int('011010111', base=2)
        expected = int('011011011', base=2)
        self.assertEqual(bits.get_next_largest(num), expected)
        print('Success: test_get_next_largest')

    def test_get_next_smallest(self):
        bits = Bits()
        self.assertRaises(Exception, bits.get_next_smallest, None)
        self.assertRaises(Exception, bits.get_next_smallest, 0)
        self.assertRaises(Exception, bits.get_next_smallest, -1)
        num = int('011010111', base=2)
        expected = int('011001111', base=2)
        self.assertEqual(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')

def main():
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
