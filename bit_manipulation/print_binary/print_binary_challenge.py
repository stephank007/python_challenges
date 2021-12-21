#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a real number between 0 and 1, print the binary representation.  If the length of the representation is > 32, return 'ERROR'.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the input a float?
#     * Yes
# * Is the output a string?
#     * Yes
# * Is 0 and 1 inclusive?
#     * No
# * Does the result include a trailing zero and decimal point?
#     * Yes
# * Is the leading zero and decimal point counted in the 32 char limit?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> 'ERROR'
# * Out of bounds (0, 1) -> 'ERROR'
# * General case
#     * 0.625 -> 0.101
#     * 0.987654321 -> 'ERROR'

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Bits(object):

    def print_binary(self, num):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_print_binary.py
import unittest


class TestBits(unittest.TestCase):

    def test_print_binary(self):
        bit = Bits()
        self.assertEqual(bit.print_binary(None), 'ERROR')
        self.assertEqual(bit.print_binary(0), 'ERROR')
        self.assertEqual(bit.print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        self.assertEqual(bit.print_binary(num), expected)
        num = 0.987654321
        self.assertEqual(bit.print_binary(num), 'ERROR')
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_print_binary()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
