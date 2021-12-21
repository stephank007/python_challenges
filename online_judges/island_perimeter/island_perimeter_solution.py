#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

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
# For each cell in the grid:
# * Check left, right, up, down
#     * For each check, if we are at the edge or the cell we are checking is land, increment sides
# 
# Complexity:
# * Time: O(rows * cols)
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def island_perimeter(self, grid):
        if grid is None:
            raise TypeError('grid cannot be None')
        sides = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    # Check left
                    if j == 0 or grid[i][j - 1] == 0:
                        sides += 1
                    # Check right
                    if j == num_cols - 1 or grid[i][j + 1] == 0:
                        sides += 1
                    # Check up
                    if i == 0 or grid[i - 1][j] == 0:
                        sides += 1
                    # Check down
                    if i == num_rows - 1 or grid[i + 1][j] == 0:
                        sides += 1
        return sides


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_island_perimeter.py', "import unittest\n\n\nclass TestIslandPerimeter(unittest.TestCase):\n\n    def test_island_perimeter(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.island_perimeter, None)\n        data = [[1, 0]]\n        expected = 4\n        self.assertEqual(solution.island_perimeter(data), expected)\n        data = [[0, 1, 0, 0],\n                [1, 1, 1, 0],\n                [0, 1, 0, 0],\n                [1, 1, 0, 0]]\n        expected = 16\n        self.assertEqual(solution.island_perimeter(data), expected)\n        print('Success: test_island_perimeter')\n\n\ndef main():\n    test = TestIslandPerimeter()\n    test.test_island_perimeter()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_island_perimeter.py')

