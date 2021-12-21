#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Island Perimeter.
# 
# See the [LeetCode](https://leetcode.com/problems/island-perimeter/) problem page.
# 
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
# 
# Example:
# 
# <pre>
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# </pre>
# 
# Answer: 16
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
#     * No, check for None
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> TypeError
# * [[1, 0]] -> 4
# * [[0, 1, 0, 0],
#    [1, 1, 1, 0],
#    [0, 1, 0, 0],
#    [1, 1, 0, 0]] -> 16
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def island_perimeter(self, grid):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_island_perimeter.py
import unittest


class TestIslandPerimeter(unittest.TestCase):

    def test_island_perimeter(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.island_perimeter, None)
        data = [[1, 0]]
        expected = 4
        self.assertEqual(solution.island_perimeter(data), expected)
        data = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]]
        expected = 16
        self.assertEqual(solution.island_perimeter(data), expected)
        print('Success: test_island_perimeter')


def main():
    test = TestIslandPerimeter()
    test.test_island_perimeter()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
