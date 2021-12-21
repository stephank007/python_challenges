#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Move all zeroes in a list to the end.
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
# * Is the output a new array of ints?
#     * No, do this in-place
# * Do we need to maintain ordering of non-zero values?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> TypeError
# * [0, 1, 0, 3, 12]
# * [1, 0] -> [1, 0]
# * [0, 1] -> [1, 0]
# * [0] -> [0]
# * [1] -> [1]
# * [1, 1] -> [1, 1]
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def move_zeroes(self, nums):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_move_zeroes.py
import unittest


class TestMoveZeroes(unittest.TestCase):

    def test_move_zeroes(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.move_zeroes, None)
        array = [0, 1, 0, 3, 12]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 3, 12, 0, 0])
        array = [1, 0]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0]
        solution.move_zeroes(array)
        self.assertEqual(array, [0])
        array = [1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1])
        array = [1, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 1])
        print('Success: test_move_zeroes')


def main():
    test = TestMoveZeroes()
    test.test_move_zeroes()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
