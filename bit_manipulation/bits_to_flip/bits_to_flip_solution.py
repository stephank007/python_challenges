#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine the number of bits to flip to convert int a to int b.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume A and B are always ints?
#     * Yes
# * Is the output an int?
#     * Yes
# * Can we assume A and B are always the same number of bits?
#     * Yes
# * Can we assume the inputs are valid (not None)?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * A or B is None -> Exception
# * General case
# <pre>
#     A = 11101
#     B = 01111
#     Result: 2
# <pre>

# ## Algorithm
# 
# We can use the xor operator to determine the bit differences between a and b
# 
# * Set count to 0
# * Set c to a xor b
# * Loop while c != 0:
#     * Increment count if the LSB in c is a 1
#         * We can check this by using a mask of 1
#     * Right shift c by 1
# * Return the count
#     
# Complexity:
# * Time: O(b), where b is the number of bits
# * Space: O(b), where b is the number of bits

# ## Code

# In[1]:


class Bits(object):

    def bits_to_flip(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        count = 0
        c = a ^ b
        while c:
            count += c & 1
            c >>= 1
        return count


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_bits_to_flip.py', "import unittest\n\n\nclass TestBits(unittest.TestCase):\n\n    def test_bits_to_flip(self):\n        bits = Bits()\n        a = int('11101', base=2)\n        b = int('01111', base=2)\n        expected = 2\n        self.assertEqual(bits.bits_to_flip(a, b), expected)\n        print('Success: test_bits_to_flip')\n\n\ndef main():\n    test = TestBits()\n    test.test_bits_to_flip()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_bits_to_flip.py')

