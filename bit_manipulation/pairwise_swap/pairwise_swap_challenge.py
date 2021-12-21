#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Swap the odd and even bits of a positive integer with as few operations as possible.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the input is always a positive int?
#     * Yes
# * Can we assume we're working with 32 bits?
#     * Yes
# * Is the output an int?
#     * Yes
# * Can we assume the inputs are valid (not None)?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * 0 -> 0
# * -1 -> -1
# * General case
# <pre>
#     input  = 1001 1111 0110
#     result = 0110 1111 1001
# <pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Bits(object):

    def pairwise_swap(self, num):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_pairwise_swap.py
import unittest


class TestBits(unittest.TestCase):

    def test_pairwise_swap(self):
        bits = Bits()
        self.assertEqual(bits.pairwise_swap(0), 0)
        self.assertEqual(bits.pairwise_swap(1), 1)
        num = int('0000100111110110', base=2)
        expected = int('0000011011111001', base=2)
        self.assertEqual(bits.pairwise_swap(num), expected)
        print('Success: test_pairwise_swap')


def main():
    test = TestBits()
    test.test_pairwise_swap()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
