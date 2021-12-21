#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given sorted arrays A, B, merge B into A in sorted order.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Does A have enough space for B?
#     * Yes
# * Can the inputs have duplicate array items?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Does the inputs also include the actual size of A and B?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * A or B is None -> Exception
# * index of last A or B < 0 -> Exception
# * A or B is empty
# * General case
#     * A = [1,  3,  5,  7,  9,  None,  None,  None]
#     * B = [4,  5,  6]
#     * A = [1, 3, 4, 5, 5, 6, 7, 9]

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/merge_into/merge_into_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Array(object):

    def merge_into(self, source, dest, source_end_index, dest_end_index):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_merge_into.py
import unittest


class TestArray(unittest.TestCase):

    def test_merge_into(self):
        array = Array()
        self.assertRaises(TypeError, array.merge_into, None, None, None, None)
        self.assertRaises(ValueError, array.merge_into, [1], [2], -1, -1)
        a = [1, 2, 3]
        self.assertEqual(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1, 2, 3]
        self.assertEqual(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1,  3,  5,  7,  9,  None,  None,  None]
        b = [4,  5,  6]
        expected = [1, 3, 4, 5, 5, 6, 7, 9]
        self.assertEqual(array.merge_into(a, b, 5, len(b)), expected)
        print('Success: test_merge_into')


def main():
    test = TestArray()
    test.test_merge_into()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
