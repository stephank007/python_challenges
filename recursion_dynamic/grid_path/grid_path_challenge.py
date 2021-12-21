#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement an algorithm to have a robot move from the upper left corner to the bottom right corner of a grid.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Are there restrictions to how the robot moves?
#     * The robot can only move right and down
# * Are some cells off limits?
#     * Yes
# * Is this a rectangular grid? i.e. the grid is not jagged?
#     * Yes
# * Will there always be a valid way for the robot to get to the bottom right?
#     * No, return None
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# o = valid cell
# x = invalid cell
# 
#    0  1  2  3
# 0  o  o  o  o
# 1  o  x  o  o
# 2  o  o  x  o
# 3  x  o  o  o
# 4  o  o  x  o
# 5  o  o  o  x
# 6  o  x  o  x
# 7  o  x  o  o
# </pre>
# 
# * General case
# 
# ```
# expected = [(0, 0), (1, 0), (2, 0),
#             (2, 1), (3, 1), (4, 1),
#             (5, 1), (5, 2), (6, 2), 
#             (7, 2), (7, 3)]
# ```
# 
# * No valid path: In above example, row 7 col 2 is also invalid -> None
# * None input -> None
# * Empty matrix -> None

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Grid(object):

    def find_path(self, matrix):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_grid_path.py
import unittest


class TestGridPath(unittest.TestCase):

    def test_grid_path(self):
        grid = Grid()
        self.assertEqual(grid.find_path(None), None)
        self.assertEqual(grid.find_path([[]]), None)
        max_rows = 8
        max_cols = 4
        matrix = [[1] * max_cols for _ in range(max_rows)]
        matrix[1][1] = 0
        matrix[2][2] = 0
        matrix[3][0] = 0
        matrix[4][2] = 0
        matrix[5][3] = 0
        matrix[6][1] = 0
        matrix[6][3] = 0
        matrix[7][1] = 0
        result = grid.find_path(matrix)
        expected = [(0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (4, 1),
                    (5, 1), (5, 2), (6, 2), 
                    (7, 2), (7, 3)]
        self.assertEqual(result, expected)
        matrix[7][2] = 0
        result = grid.find_path(matrix)
        self.assertEqual(result, None)
        print('Success: test_grid_path')


def main():
    test = TestGridPath()
    test.test_grid_path()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
