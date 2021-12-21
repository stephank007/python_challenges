#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given two 16 bit numbers, n and m, and two indices i, j, insert m into n such that m starts at bit j and ends at bit i.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume j > i?
#     * Yes
# * Can we assume i through j have enough space for m?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None as an input -> Exception
# * Negative index for i or j -> Exception
# * General case
# 
# <pre>
# i = 2, j = 6
#                     j    i
# n      = 0000 0100 0011 1101
# m      = 0000 0000 0001 0011
# result = 0000 0100 0100 1101
# </pre>

# ## Algorithm
# 
# <pre>
#                     j    i
# n      = 0000 0100 0011 1101
# m      = 0000 0000 0001 0011
# 
# lmask  = 1111 1111 1111 1111  -1
# lmask  = 1111 1111 1000 0000  -1 << (j + 1)
# 
# rmask  = 0000 0000 0000 0001   1
# rmask  = 0000 0000 0000 0100   1 << i
# rmask  = 0000 0000 0000 0011   (1 << i) -1
# 
# mask   = 1111 1111 1000 0011   lmask | rmask
# 
# n      = 0000 0100 0011 1101
# mask   = 1111 1111 1000 0011   n & mask 
# --------------------------------------------------
# n2     = 0000 0100 0000 0001
# 
# n2     = 0000 0100 0000 0001
# mask2  = 0000 0000 0100 1100   m << i
# --------------------------------------------------
# result = 0000 0100 0100 1101   n2 | mask2
# </pre>
# 
# Complexity:
# * Time: O(b), where b is the number of bits
# * Space: O(b), where b is the number of bits

# ## Code

# In[1]:


class Bits(object):

    def insert_m_into_n(self, m, n, i, j):
        if None in (m, n, i, j):
            raise TypeError('Argument cannot be None')
        if i < 0 or j < 0:
            raise ValueError('Index cannot be negative')
        left_mask = -1 << (j + 1)
        right_mask = (1 << i) - 1
        n_mask = left_mask | right_mask
        # Clear bits from j to i, inclusive
        n_cleared = n & n_mask
        # Shift m into place before inserting it into n
        m_mask = m << i
        return n_cleared | m_mask


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_insert_m_into_n.py', "import unittest\n\n\nclass TestBit(unittest.TestCase):\n\n    def test_insert_m_into_n(self):\n        n = int('0000010000111101', base=2)\n        m = int('0000000000010011', base=2)\n        expected = int('0000010001001101', base=2)\n        bits = Bits()\n        self.assertEqual(bits.insert_m_into_n(m, n, i=2, j=6), expected)\n        print('Success: test_insert_m_into_n')\n\n\ndef main():\n    test = TestBit()\n    test.test_insert_m_into_n()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_insert_m_into_n.py')

