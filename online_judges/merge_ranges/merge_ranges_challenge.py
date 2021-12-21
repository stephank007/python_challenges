#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a list of tuples representing ranges, condense the ranges.  
# 
# Example: [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Are the tuples in sorted order?
#     * No
# * Are the tuples ints?
#     * Yes
# * Will all tuples have the first element less than the second?
#     * Yes
# * Is there an upper bound on the input range?
#     * No
# * Is the output a list of tuples?
#     * Yes
# * Is the output a new array?
#     * Yes
# * Can we assume the inputs are valid?
#     * No, check for None
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None input -> TypeError
# * [] - []
# * [(2, 3), (7, 9)] -> [(2, 3), (7, 9)]
# * [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]
# * [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)] -> [(1, 11)]
# * [(2, 3), (3, 8), (7, 9), (8, 10)] -> [(2, 10)]
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def merge_ranges(self, array):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_merge_ranges.py
import unittest


class TestMergeRanges(unittest.TestCase):

    def test_merge_ranges(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.merge_ranges, None)
        self.assertEqual(solution.merge_ranges([]), [])
        array = [(2, 3), (7, 9)]
        expected = [(2, 3), (7, 9)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(2, 3), (3, 5), (7, 9), (8, 10)]
        expected = [(2, 5), (7, 10)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)]
        expected = [(1, 11)]
        self.assertEqual(solution.merge_ranges(array), expected)
        print('Success: test_merge_ranges')


def main():
    test = TestMergeRanges()
    test.test_merge_ranges()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
