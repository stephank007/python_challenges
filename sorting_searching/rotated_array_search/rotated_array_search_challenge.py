#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find an element in a sorted array that has been rotated a number of times.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the input an array of ints?
#     * Yes
# * Do we know how many times the array was rotated?
#     * No
# * Was the array originally sorted in increasing or decreasing order?
#     * Increasing
# * For the output, do we return the index?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * [] -> None
# * Not found -> None
# * General case with duplicates
# * General case without duplicates

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/rotated_array_search/rotated_array_search_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Array(object):

    def search_sorted_array(self, array, val):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_search_sorted_array.py
import unittest


class TestArray(unittest.TestCase):

    def test_search_sorted_array(self):
        array = Array()
        self.assertRaises(TypeError, array.search_sorted_array, None)
        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)
        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)
        data = [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
        self.assertEqual(array.search_sorted_array(data, val=1), 3)
        data = [ 1,  1,  2,  1,  1,  1,  1,  1,  1,  1]
        self.assertEqual(array.search_sorted_array(data, val=2), 2)
        print('Success: test_search_sorted_array')


def main():
    test = TestArray()
    test.test_search_sorted_array()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
