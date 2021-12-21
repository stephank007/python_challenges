#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given a list of tuples representing ranges, condense the ranges.  
# 
# Example: [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# * Sort the tuples based on start time
# * Check each adjacent tuple to see if they can be merged
# 
# <pre>
# Case: * [(2, 3), (3, 8), (7, 9), (8, 10)] -> [(2, 10)]
# 
# * Sort by start time (already sorted)
# * Add the first tuple to the merged_array
# * Loop through each item in sorted_array starting at index 1
#     * If there is no overlap
#         * Add the current item to merged_array
#     * Else
#         * Update the last item in merged_array
#             * The end time will be the max of merged_array[-1][1] and sorted_array[i][1]
# 
# Start:
#                            i
#                    0       1       2       3
# sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
# merged_array = [(2, 3)]
# 
# Overlap with (2, 3), (3, 8):
#                            i
#                    0       1       2       3
# sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
# merged_array = [(2, 8)]
# 
# Overlap with (2, 8), (7, 9):
#                                    i
#                    0       1       2       3
# sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
# merged_array = [(2, 9)]
# 
# Overlap with (2, 9) (8, 10):
#                                    i
#                    0       1       2       3
# sorted_array = [(2, 3), (3, 8), (7, 9), (8, 10)]
# merged_array = [(2, 10)]
# </pre>
# 
# Complexity:
# * Time: O(n log(n))
# * Space: O(n)

# ## Code

# In[1]:


class Solution(object):

    def merge_ranges(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if not array:
            return array
        sorted_array = sorted(array)
        merged_array = [sorted_array[0]]
        for index, item in enumerate(sorted_array):
            if index == 0:
                continue
            start_prev, end_prev = merged_array[-1]
            start_curr, end_curr = item
            if end_prev < start_curr:
                # No overlap, add the entry
                merged_array.append(item)
            else:
                # Overlap, update the previous entry's end value
                merged_array[-1] = (start_prev, max(end_prev, end_curr))
        return merged_array


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_merge_ranges.py', "import unittest\n\n\nclass TestMergeRanges(unittest.TestCase):\n\n    def test_merge_ranges(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.merge_ranges, None)\n        self.assertEqual(solution.merge_ranges([]), [])\n        array = [(2, 3), (7, 9)]\n        expected = [(2, 3), (7, 9)]\n        self.assertEqual(solution.merge_ranges(array), expected)\n        array = [(3, 5), (2, 3), (7, 9), (8, 10)]\n        expected = [(2, 5), (7, 10)]\n        self.assertEqual(solution.merge_ranges(array), expected)\n        array = [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)]\n        expected = [(1, 11)]\n        self.assertEqual(solution.merge_ranges(array), expected)\n        print('Success: test_merge_ranges')\n\n\ndef main():\n    test = TestMergeRanges()\n    test.test_merge_ranges()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_merge_ranges.py')

