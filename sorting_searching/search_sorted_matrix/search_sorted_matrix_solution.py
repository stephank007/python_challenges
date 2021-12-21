#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Search a sorted matrix for an item.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# <pre>
# 
# Find 60 (val = 60)
# 
#  20  40  63   80
#  30  50  80   90
#  40  60  100 110
#  50  65  105 150
# 
# * If the start of a col > val, look left
# * If the end of a col < val, look right
# * If the start of row > val, look up
# * If the end of a row < val, look down
# 
# If we start at the upper right corner, we just need to use these cases:
# 
# * If the start of a col > val, look left
# * If the end of a row < val, look down
# 
# </pre>
# 
# Complexity:
# * Time: O(n + m), where n and m are the matrix dimensions
# * Space: O(1)

# ## Code

# In[1]:


class SortedMatrix(object):

    def find_val(self, matrix, val):
        if matrix is None or val is None:
            raise TypeError('matrix and val cannot be None')
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == val:
                return (row, col)
            elif matrix[row][col] > val:
                col -= 1
            else:
                row += 1
        return None


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_search_sorted_matrix.py', "import unittest\n\n\nclass TestSortedMatrix(unittest.TestCase):\n\n    def test_find_val(self):\n        matrix = [[20, 40, 63, 80],\n                  [30, 50, 80, 90],\n                  [40, 60, 110, 110],\n                  [50, 65, 105, 150]]\n        sorted_matrix = SortedMatrix()\n        self.assertRaises(TypeError, sorted_matrix.find_val, None, None)\n        self.assertEqual(sorted_matrix.find_val(matrix, 1000), None)\n        self.assertEqual(sorted_matrix.find_val(matrix, 60), (2, 1))\n        print('Success: test_find_val')\n\n\ndef main():\n    test = TestSortedMatrix()\n    test.test_find_val()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_search_sorted_matrix.py')

