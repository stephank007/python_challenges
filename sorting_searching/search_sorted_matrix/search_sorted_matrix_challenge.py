#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Search a sorted matrix for an item.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Are items in each row sorted?
#     * Yes
# * Are items in each column sorted?
#     * Yes
# * Is the sorting in ascending or descending order?
#     * Ascending
# * Is the matrix a rectangle?  Not jagged?
#     * Yes
# * Is the matrix square?
#     * Not necessarily
# * Is the output a tuple (row, col)?
#     * Yes
# * Is the item you are searching for always in the matrix?
#     * No
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * General case
#     * Item found -> (row, col)
#     * Item not found -> None

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/search_sorted_matrix/search_sorted_matrix_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class SortedMatrix(object):

    def find_val(self, matrix, val):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_search_sorted_matrix.py
import unittest


class TestSortedMatrix(unittest.TestCase):

    def test_find_val(self):
        matrix = [[20, 40, 63, 80],
                  [30, 50, 80, 90],
                  [40, 60, 110, 110],
                  [50, 65, 105, 150]]
        sorted_matrix = SortedMatrix()
        self.assertRaises(TypeError, sorted_matrix.find_val, None, None)
        self.assertEqual(sorted_matrix.find_val(matrix, 1000), None)
        self.assertEqual(sorted_matrix.find_val(matrix, 60), (2, 1))
        print('Success: test_find_val')


def main():
    test = TestSortedMatrix()
    test.test_find_val()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
