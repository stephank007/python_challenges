#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement common bit manipulation operations: get_bit, set_bit, clear_bit, clear_bits_msb_to_index, clear_bits_msb_to_lsb, update_bit.
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
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None as a number input -> Exception
# * Negative index -> Exception
# 
# ### get_bit
#     number   = 0b10001110, index = 3
#     expected = True
# ### set_bit
#     number   = 0b10001110, index = 4
#     expected = 0b10011110
# ### clear_bit
#     number   = 0b10001110, index = 3
#     expected = 0b10000110
# ### clear_bits_msb_to_index
#     number   = 0b10001110, index = 3
#     expected = 0b00000110
# ### clear_bits_index_to_lsb
#     number   = 0b10001110, index = 3
#     expected = 0b10000000
# ### update_bit
#     number   = 0b10001110, index = 3, value = 1
#     expected = 0b10001110
#     number   = 0b10001110, index = 3, value = 0
#     expected = 0b10000110
#     number   = 0b10001110, index = 0, value = 1
#     expected = 0b10001111

# ## Algorithm
# 
# ### get_bit
# 
# <pre>
# indices  7 6 5 4  3 2 1 0  index = 3
# --------------------------------------------------
# input    1 0 0 0  1 1 1 0  0b10001110
# mask     0 0 0 0  1 0 0 0  1 << index
# --------------------------------------------------
# result   0 0 0 0  1 0 0 0  number & mask != 0
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# ### set_bit
# 
# <pre>
# indices  7 6 5 4  3 2 1 0  index = 4
# --------------------------------------------------
# input    1 0 0 0  1 1 1 0  0b10001110
# mask     0 0 0 1  0 0 0 0  1 << index
# --------------------------------------------------
# result   1 0 0 1  1 1 1 0  number | mask
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# ### clear_bit
# 
# <pre>
# indices  7 6 5 4  3 2 1 0  index = 3
# --------------------------------------------------
# input    1 0 0 0  1 1 1 0  0b10001110
# mask     0 0 0 0  1 0 0 0  1 << index
# mask     1 1 1 1  0 1 1 1  ~(1 << index)
# --------------------------------------------------
# result   1 0 0 0  0 1 1 0  number & mask
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# ### clear_bits_msb_to_index
# 
# <pre>
# indices  7 6 5 4  3 2 1 0  index = 3
# --------------------------------------------------
# input    1 0 0 0  1 1 1 0  0b10001110
# mask     0 0 0 0  1 0 0 0  1 << index
# mask     0 0 0 0  0 1 1 1  (1 << index) - 1
# --------------------------------------------------
# result   0 0 0 0  0 1 1 1  number & mask
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# ### clear_bits_index_to_lsb
# 
# <pre>
# indices  7 6 5 4  3 2 1 0  index = 3
# --------------------------------------------------
# input    1 0 0 0  1 1 1 0  0b10001110
# mask     0 0 0 1  0 0 0 0  1 << index + 1
# mask     0 0 0 0  1 1 1 1  (1 << index + 1) - 1
# mask     1 1 1 1  0 0 0 0  ~((1 << index + 1) - 1)
# --------------------------------------------------
# result   1 0 0 0  0 0 0 0  number & mask
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# ### update_bit
# 
# * Use `get_bit` to see if the value is already set or cleared
# * If not, use `set_bit` if setting the value or `clear_bit` if clearing the value
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# 
# 

# ## Code

# In[1]:


def validate_index(func):
    def validate_index_wrapper(self, *args, **kwargs):
        for arg in args:
            if arg < 0:
                raise IndexError('Invalid index')
        return func(self, *args, **kwargs)
    return validate_index_wrapper


# In[2]:


class Bit(object):

    def __init__(self, number):
        if number is None:
            raise TypeError('number cannot be None')
        self.number = number

    @validate_index
    def get_bit(self, index):
        mask = 1 << index
        return self.number & mask != 0

    @validate_index
    def set_bit(self, index):
        mask = 1 << index
        self.number |= mask
        return self.number

    @validate_index
    def clear_bit(self, index):
        mask = ~(1 << index)
        self.number &= mask
        return self.number

    @validate_index
    def clear_bits_msb_to_index(self, index):
        mask = (1 << index) - 1
        self.number &= mask
        return self.number

    @validate_index
    def clear_bits_index_to_lsb(self, index):
        mask = ~((1 << index + 1) - 1)
        self.number &= mask
        return self.number

    @validate_index
    def update_bit(self, index, value):
        if value is None or value not in (0, 1):
            raise Exception('Invalid value')
        if self.get_bit(index) == value:
            return self.number
        if value:
            self.set_bit(index)
        else:
            self.clear_bit(index)
        return self.number


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_bit.py', "import unittest\n\n\nclass TestBit(unittest.TestCase):\n\n    def test_bit(self):\n        number = int('10001110', base=2)\n        bit = Bit(number)\n        self.assertEqual(bit.get_bit(index=3), True)\n        expected = int('10011110', base=2)\n        self.assertEqual(bit.set_bit(index=4), expected)\n        bit = Bit(number)\n        expected = int('10000110', base=2)\n        self.assertEqual(bit.clear_bit(index=3), expected)\n        bit = Bit(number)\n        expected = int('00000110', base=2)\n        self.assertEqual(bit.clear_bits_msb_to_index(index=3), expected)\n        bit = Bit(number)\n        expected = int('10000000', base=2)\n        self.assertEqual(bit.clear_bits_index_to_lsb(index=3), expected)\n        bit = Bit(number)\n        self.assertEqual(bit.update_bit(index=3, value=1), number)\n        bit = Bit(number)\n        expected = int('10000110', base=2)\n        self.assertEqual(bit.update_bit(index=3, value=0), expected)\n        bit = Bit(number)\n        expected = int('10001111', base=2)\n        self.assertEqual(bit.update_bit(index=0, value=1), expected)\n        print('Success: test_bit')\n\n\ndef main():\n    test = TestBit()\n    test.test_bit()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_bit.py')

