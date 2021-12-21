#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the magic index in an array, where array[i] = i.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the array sorted?
#     * Yes
# * Are the elements in the array distinct?
#     * No
# * Does a magic index always exist?
#     * No
# * If there is no magic index, do we just return -1?
#     * Yes
# * Are negative values allowed in the array?
#     * Yes
# * If there are multiple magic values, what do we return?
#     * Return the left-most one
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None input -> -1
# * Empty array -> -1
# 
# <pre>
# a[i]  -4 -2  2  6  6  6  6 10
#   i    0  1  2  3  4  5  6  7
# </pre>
# 
# Result: 2
# 
# <pre>
# a[i]  -4 -2  1  6  6  6  6 10
#   i    0  1  2  3  4  5  6  7
# </pre>
# 
# Result: 6
# 
# <pre>
# a[i]  -4 -2  1  6  6  6  7 10
#   i    0  1  2  3  4  5  6  7
# </pre>
# 
# Result: -1

# ## Algorithm
# 
# We'll use a binary search to split the search space in half on each iteration.  To obtain more efficiency, we can do a little better than a naive left and half split.
# 
# In the example below, we see that i == 5 cannot be the magic index, otherwise a[5] would have to equal 5 (note a[4] == 6).
# 
# <pre>
# a[i]  -4 -2  2  6  6  6  6 10
#   i    0  1  1  3  4  5  6  7
#                   mid
# </pre>
# 
# Similarly, in the example below we can further trim the left search space.
# 
# <pre>
# a[i]  -4 -2  2  2  2  6  6 10
#   i    0  1  2  3  4  5  6  7
#                   mid
# </pre>
# 
# 
# * Calculate mid
# * If mid == array[mid], return mid
# * Recurse on the left side of the array
#     * start: 0
#     * end: min(mid-1, array[mid]
# * Recurse on the right side of the array
#     * start: max(mid+1, array[mid]
#     * end: end
# 
# Complexity:
# * Time: O(log(n))
# * Space: O(log(n))

# ## Code

# In[1]:


from __future__ import division


class MagicIndex(object):

    def find_magic_index(self, array):
        if array is None or not array:
            return -1
        return self._find_magic_index(array, 0, len(array) - 1)

    def _find_magic_index(self, array, start, end):
        if end < start or start < 0 or end >= len(array):
            return -1
        mid = (start + end) // 2
        if mid == array[mid]:
            return mid
        left_end = min(mid - 1, array[mid])
        left_result = self._find_magic_index(array, start, end=left_end)
        if left_result != -1:
            return left_result
        right_start = max(mid + 1, array[mid])
        right_result = self._find_magic_index(array, start=right_start, end=end)
        if right_result != -1:
            return right_result
        return -1


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_find_magic_index.py', "import unittest\n\n\nclass TestFindMagicIndex(unittest.TestCase):\n\n    def test_find_magic_index(self):\n        magic_index = MagicIndex()\n        self.assertEqual(magic_index.find_magic_index(None), -1)\n        self.assertEqual(magic_index.find_magic_index([]), -1)\n        array = [-4, -2, 2, 6, 6, 6, 6, 10]\n        self.assertEqual(magic_index.find_magic_index(array), 2)\n        array = [-4, -2, 1, 6, 6, 6, 6, 10]\n        self.assertEqual(magic_index.find_magic_index(array), 6)\n        array = [-4, -2, 1, 6, 6, 6, 7, 10]\n        self.assertEqual(magic_index.find_magic_index(array), -1)\n        print('Success: test_find_magic')\n\n\ndef main():\n    test = TestFindMagicIndex()\n    test.test_find_magic_index()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_find_magic_index.py')

