#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find an element in a sorted array that has been rotated a number of times.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the input an array of ints?
#     * Yes
# * Can the input have duplicates?
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
# ### General case without dupes
# 
# <pre>
# 
# index                   0   1   2   3   4   5   6   7   8   9
# input                 [ 1,  3,  5,  6,  7,  8,  9, 10, 12, 14]
# input rotated 1x      [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
# input rotated 2x      [ 5,  6,  7,  8,  9, 10, 12, 14,  1,  3]
# input rotated 3x      [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
# 
# find 1
# len = 10
# mid = 10 // 2 = 5
#                         s                   m               e
# index                   0   1   2   3   4   5   6   7   8   9
# input                 [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
# 
# input[start] > input[mid]: Left half is rotated
# input[end] >= input[mid]: Right half is sorted
# 1 is not within input[mid+1] to input[end] on the right side, go left
# 
#                         s       m       e
# index                   0   1   2   3   4   5   6   7   8   9
# input                 [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
# 
# input[start] <= input[mid]: Right half is rotated
# input[end] >= input[mid]: Left half is sorted
# 1 is not within input[left] to input[mid-1] on the left side, go right
# 
# </pre>
# 
# ### General case with dupes
# 
# <pre>
# 
#                         s                   m               e
# index                   0   1   2   3   4   5   6   7   8   9
# input                 [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  2]
# 
# input[start] == input[mid], input[mid] != input[end], go right
# 
# input rotated 1x      [ 1,  1,  2,  1,  1,  1,  1,  1,  1,  1]
# 
# input[start] == input[mid] == input[end], search both sides
# 
# </pre>
# 
# Complexity:
# * Time: O(log n) if there are no duplicates, else O(n)
# * Space: O(m), where m is the recursion depth

# ## Code

# In[1]:


class Array(object):

    def search_sorted_array(self, array, val):
        if array is None or val is None:
            raise TypeError('array or val cannot be None')
        if not array:
            return None
        return self._search_sorted_array(array, val, start=0, end=len(array) - 1)

    def _search_sorted_array(self, array, val, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        if array[mid] == val:
            return mid
        # Left side is sorted
        if array[start] < array[mid]:
            if array[start] <= val < array[mid]:
                return self._search_sorted_array(array, val, start, mid - 1)
            else:
                return self._search_sorted_array(array, val, mid + 1, end)
        # Right side is sorted
        elif array[start] > array[mid]:
            if array[mid] < val <= array[end]:
                return self._search_sorted_array(array, val, mid + 1, end)
            else:
                return self._search_sorted_array(array, val, start, mid - 1)
        # Duplicates
        else:
            if array[mid] != array[end]:
                return self._search_sorted_array(array, val, mid + 1, end)
            else:
                result = self._search_sorted_array(array, val, start, mid - 1)
                if result != None:
                    return result
                else:
                    return self._search_sorted_array(array, val, mid + 1, end)


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_search_sorted_array.py', "import unittest\n\n\nclass TestArray(unittest.TestCase):\n\n    def test_search_sorted_array(self):\n        array = Array()\n        self.assertRaises(TypeError, array.search_sorted_array, None)\n        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)\n        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)\n        data = [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]\n        self.assertEqual(array.search_sorted_array(data, val=1), 3)\n        data = [ 1,  1,  2,  1,  1,  1,  1,  1,  1,  1]\n        self.assertEqual(array.search_sorted_array(data, val=2), 2)\n        print('Success: test_search_sorted_array')\n\n\ndef main():\n    test = TestArray()\n    test.test_search_sorted_array()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_search_sorted_array.py')

