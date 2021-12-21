#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given a positive integer, get the next largest number and the next smallest number with the same number of 1's as the given number.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# ### get_next_largest
# 
# * Find the right-most non trailing zero, call this index
#     * We'll use a mask of 1 and do a logical right shift on a copy of num to examine each bit starting from the right
#     * Count the number of zeroes to the right of index
#         * While num & 1 == 0 and num_copy != 0:
#             * Increment number of zeroes
#             * Logical shift right num_copy
#     * Count the number of ones to the right of index
#         * While num & 1 == 1 and num_copy != 0:
#             * Increment number of ones
#             * Logical shift right num_copy
#     * The index will be the sum of number of ones and number of zeroes
#     * Set the index bit
#     * Clear all bits to the right of index
#     * Set bits starting from 0
#         * Only set (number of ones - 1) bits because we set index to 1
# 
# We should make a note that Python does not have a logical right shift operator built in.  We can either use a positive number of implement one for a 32 bit number:
# 
#     num % 0x100000000 >> n
# 
# ### get_next_smallest
# 
# * The algorithm for finding the next smallest number is very similar to finding the next largest number
#     * Instead of finding the right-most non-trailing zero, we'll find the right most non-trailing one and clear it
#     * Clear all bits to the right of index
#     * Set bits starting at 0 to the number of ones to the right of index, plus one
# 
# Complexity:
# * Time: O(b), where b is the number of bits in num
# * Space: O(b), where b is the number of bits in num

# ## Code

# In[1]:


class Bits(object):

    def get_next_largest(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num <= 0:
            raise ValueError('num cannot be 0 or negative')
        num_ones = 0
        num_zeroes = 0
        num_copy = num
        # We'll look for index, which is the right-most non-trailing zero
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 0:
            num_zeroes += 1
            num_copy >>= 1
        # Count number of ones to the right of index
        while num_copy != 0 and num_copy & 1 == 1:
            num_ones += 1
            num_copy >>= 1
        # Determine index and set the bit
        index = num_zeroes + num_ones
        num |= 1 << index
        # Clear all bits to the right of index
        num &= ~((1 << index) - 1)
        # Set bits starting from 0
        num |= ((1 << num_ones - 1) - 1)
        return num

    def get_next_smallest(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num <= 0:
            raise ValueError('num cannot be 0 or negative')
        num_ones = 0
        num_zeroes = 0
        num_copy = num
        # We'll look for index, which is the right-most non-trailing one
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 1:
            num_ones += 1
            num_copy >>= 1
        # Count number of zeroes to the right of index
        while num_copy != 0 and num_copy & 1 == 0:
            num_zeroes += 1
            num_copy >>= 1
        # Determine index and clear the bit
        index = num_zeroes + num_ones
        num &= ~(1 << index)
        # Clear all bits to the right of index
        num &= ~((1 << index) - 1)
        # Set bits starting from 0
        num |= (1 << num_ones + 1) - 1
        return num


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_get_next_largest.py', "import unittest\n\n\nclass TestBits(unittest.TestCase):\n\n    def test_get_next_largest(self):\n        bits = Bits()\n        self.assertRaises(Exception, bits.get_next_largest, None)\n        self.assertRaises(Exception, bits.get_next_largest, 0)\n        self.assertRaises(Exception, bits.get_next_largest, -1)\n        num = int('011010111', base=2)\n        expected = int('011011011', base=2)\n        self.assertEqual(bits.get_next_largest(num), expected)\n        print('Success: test_get_next_largest')\n\n    def test_get_next_smallest(self):\n        bits = Bits()\n        self.assertRaises(Exception, bits.get_next_smallest, None)\n        self.assertRaises(Exception, bits.get_next_smallest, 0)\n        self.assertRaises(Exception, bits.get_next_smallest, -1)\n        num = int('011010111', base=2)\n        expected = int('011001111', base=2)\n        self.assertEqual(bits.get_next_smallest(num), expected)\n        print('Success: test_get_next_smallest')\n\ndef main():\n    test = TestBits()\n    test.test_get_next_largest()\n    test.test_get_next_smallest()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_get_next_largest.py')

