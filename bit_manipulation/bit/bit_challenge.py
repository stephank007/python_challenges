#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement common bit manipulation operations: get_bit, set_bit, clear_bit, clear_bits_msb_to_index, clear_bits_msb_to_lsb, update_bit.
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
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Bit(object):

    def __init__(self, number):
        # TODO: Implement me
        pass

    def get_bit(self, index):
        # TODO: Implement me
        pass

    def set_bit(self, index):
        # TODO: Implement me
        pass

    def clear_bit(self, index):
        # TODO: Implement me
        pass

    def clear_bits_msb_to_index(self, index):
        # TODO: Implement me
        pass

    def clear_bits_index_to_lsb(self, index):
        # TODO: Implement me
        pass

    def update_bit(self, index, value):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_bit.py
import unittest


class TestBit(unittest.TestCase):

    def test_bit(self):
        number = int('10001110', base=2)
        bit = Bit(number)
        self.assertEqual(bit.get_bit(index=3), True)
        expected = int('10011110', base=2)
        self.assertEqual(bit.set_bit(index=4), expected)
        bit = Bit(number)
        expected = int('10000110', base=2)
        self.assertEqual(bit.clear_bit(index=3), expected)
        bit = Bit(number)
        expected = int('00000110', base=2)
        self.assertEqual(bit.clear_bits_msb_to_index(index=3), expected)
        bit = Bit(number)
        expected = int('10000000', base=2)
        self.assertEqual(bit.clear_bits_index_to_lsb(index=3), expected)
        bit = Bit(number)
        self.assertEqual(bit.update_bit(index=3, value=1), number)
        bit = Bit(number)
        expected = int('10000110', base=2)
        self.assertEqual(bit.update_bit(index=3, value=0), expected)
        bit = Bit(number)
        expected = int('10001111', base=2)
        self.assertEqual(bit.update_bit(index=0, value=1), expected)
        print('Success: test_bit')


def main():
    test = TestBit()
    test.test_bit()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
