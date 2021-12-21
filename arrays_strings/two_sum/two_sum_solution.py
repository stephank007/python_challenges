#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given an array, find the two indices that sum to a specific value.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is there exactly one solution?
#     * Yes
# * Is there always a solution?
#     * Yes
# * Is the array an array of ints?
#     * Yes
# * Is the array sorted?
#     No
# * Are negative values possible?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None input -> TypeError
# * [] -> ValueError
# * [1, 3, 2, -7, 5], 7 -> [2, 4]

# ## Algorithm
# 
# ### Brute force
# 
# * For i in range(len(input)):
#     * For j in range(i+1, len(input)):
#         * if i + j == target return True
# * return False
# 
# Complexity:
# * Time: O(n^2)
# * Space: O(1)
# 
# ### Optimized
# 
# <pre>
# * Loop through each num in nums
#     * Calculate the cache_target = target - num
# 
# target = 7
# index  =  0  1  2   3  4
# nums   = [1, 3, 2, -7, 5]
#           ^
# cache_target = 7 - 1 = 6
# cache
# 6 -> 0
# 
# 1 not in cache
# 
# index  =  0  1  2   3  4
# nums   = [1, 3, 2, -7, 5]
#              ^
# cache_target = 7 - 3 = 4
# cache
# 6 -> 0
# 4 -> 1
# 
# 3 not in cache
# 
# index  =  0  1  2   3  4
# nums   = [1, 3, 2, -7, 5]
#                 ^
# cache_target = 7 - 2 = 5
# cache
# 6 -> 0
# 4 -> 1
# 5 -> 2
# 
# 2 not in cache
# 
# index  =  0  1  2   3  4
# nums   = [1, 3, 2, -7, 5]
#                     ^
# cache_target = 7 + 7 = 14
# cache
# 6  -> 0
# 4  -> 1
# 5  -> 2
# 14 -> 3
# 
# -7 not in cache
# 
# index  =  0  1  2   3  4
# nums   = [1, 3, 2, -7, 5]
#                        ^
# cache_target = 7 - 5 = 2
# cache
# 6  -> 0
# 4  -> 1
# 5  -> 2
# 14 -> 3
# 
# 5 in cache, success, output matching indices: cache[num] and current iteration index
# 
# output = [2, 4]
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Code

# In[1]:


class Solution(object):

    def two_sum(self, nums, target):
        if nums is None or target is None:
            raise TypeError('nums or target cannot be None')
        if not nums:
            raise ValueError('nums cannot be empty')
        cache = {}
        for index, num in enumerate(nums):
            cache_target = target - num
            if num in cache:
                return [cache[num], index]
            else:
                cache[cache_target] = index
        return None


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_two_sum.py', "import unittest\n\n\nclass TestTwoSum(unittest.TestCase):\n\n    def test_two_sum(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.two_sum, None, None)\n        self.assertRaises(ValueError, solution.two_sum, [], 0)\n        target = 7\n        nums = [1, 3, 2, -7, 5]\n        expected = [2, 4]\n        self.assertEqual(solution.two_sum(nums, target), expected)\n        print('Success: test_two_sum')\n\n\ndef main():\n    test = TestTwoSum()\n    test.test_two_sum()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_two_sum.py')

