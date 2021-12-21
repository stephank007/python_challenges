#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Swap the odd and even bits of a positive integer with as few operations as possible.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
#     input  = 0000 1001 1111 0110
#     result = 0000 0110 1111 1001
# <pre>

# ## Algorithm
# 
# <pre>
# * Isolate the odd bits with a mask:
#     0000 1001 1111 0110  num
#     1010 1010 1010 1010  mask
#     --------------------------------
#     0000 1000 1010 0010  num & mask
# 
# * Shift the odd bits right:
#     0000 0100 0101 0001  odd
# 
# * Isolate the even bits with a mask:
#     0000 1001 1111 0110  num
#     0101 0101 0101 0101  mask
#     --------------------------------
#     0000 0001 0101 0100  num & mask
# 
# * Shift the even bits left:
#     0000 0010 1010 1000  even
# 
# * Return even | odd
#     0000 0100 0101 0001  odd
#     0000 0010 1010 1000  even
#     --------------------------------
#     0000 0110 1111 1001  odd | even
# </pre>
# 
# Complexity:
# * Time: O(b), where b is the number of bits
# * Space: O(b), where b is the number of bits

# ## Code

# In[1]:


class Bits(object):

    def pairwise_swap(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num == 0 or num == 1:
            return num
        odd = (num & int('1010101010101010', base=2)) >> 1
        even = (num & int('0101010101010101', base=2)) << 1
        return odd | even


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_pairwise_swap.py', "import unittest\n\n\nclass TestBits(unittest.TestCase):\n\n    def test_pairwise_swap(self):\n        bits = Bits()\n        self.assertEqual(bits.pairwise_swap(0), 0)\n        self.assertEqual(bits.pairwise_swap(1), 1)\n        num = int('0000100111110110', base=2)\n        expected = int('0000011011111001', base=2)\n        self.assertEqual(bits.pairwise_swap(num), expected)\n        self.assertRaises(TypeError, bits.pairwise_swap, None)\n        \n        print('Success: test_pairwise_swap')\n\n\ndef main():\n    test = TestBits()\n    test.test_pairwise_swap()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_pairwise_swap.py')

