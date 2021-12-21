#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given an array of 32 integers, find an int not in the input.  Use a minimal amount of memory.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Are we working with non-negative ints?
#     * Yes
# * What is the range of the integers?
#     * Discuss the approach for 4 billion integers
#     * Implement for 32 integers
# * Can we assume the inputs are valid?
#     * No

# ## Test Cases
# 
# * None -> Exception
# * [] -> Exception
# * General case
#     * There is an int excluded from the input -> int
#     * There isn't an int excluded from the input -> None

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/new_int/new_int_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


from bitstring import BitArray  # run pip install bitstring


class Bits(object):

    def new_int(self, array, max_size):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_new_int.py
import unittest


class TestBits(unittest.TestCase):

    def test_new_int(self):
        bits = Bits()
        max_size = 32
        self.assertRaises(TypeError, bits.new_int, None, max_size)
        self.assertRaises(TypeError, bits.new_int, [], max_size)
        data = [item for item in range(30)]
        data.append(31)
        self.assertEqual(bits.new_int(data, max_size), 30)
        data = [item for item in range(32)]
        self.assertEqual(bits.new_int(data, max_size), None)
        print('Success: test_find_int_excluded_from_input')


def main():
    test = TestBits()
    test.test_new_int()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
