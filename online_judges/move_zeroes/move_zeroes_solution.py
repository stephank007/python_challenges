#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Move all zeroes in a list to the end.
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
# * [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
# * [1, 0] -> [1, 0]
# * [0, 1] -> [1, 0]
# * [0] -> [0]
# * [1] -> [1]
# * [1, 1] -> [1, 1]
# </pre>

# ## Algorithm
# 
# * pos = 0
# * Loop through each item in the input
#     * If the item != 0, set input[pos] = item
#         * pos++
# * Fill input[pos:] with zeroes
# 
# <pre>
#  |
# [0, 1, 0, 3, 12]
#  ^
#     |
# [0, 1, 0, 3, 12]
#  ^
#     |
# [1, 1, 0, 3, 12]
#  ^
#        |
# [1, 1, 0, 3, 12]
#     ^
#           |
# [1, 1, 0, 3, 12]
#     ^
#           |
# [1, 3, 0, 3, 12]
#     ^
#               |
# [1, 3, 0, 3, 12]
#        ^
#               |
# [1, 3, 12, 3, 12]
#        ^
# 
# Fill right with zeroes:
# 
# [1, 3, 12, 3, 12]
#            ^
# [1, 3, 12, 0, 12]
#            ^
# [1, 3, 12, 0, 0]
#               ^
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def move_zeroes(self, nums):
        if nums is None:
            raise TypeError('nums cannot be None')
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        if pos < len(nums):
            nums[pos:] = [0] * (len(nums) - pos)


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_move_zeroes.py', "import unittest\n\n\nclass TestMoveZeroes(unittest.TestCase):\n\n    def test_move_zeroes(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.move_zeroes, None)\n        array = [0, 1, 0, 3, 12]\n        solution.move_zeroes(array)\n        self.assertEqual(array, [1, 3, 12, 0, 0])\n        array = [1, 0]\n        solution.move_zeroes(array)\n        self.assertEqual(array, [1, 0])\n        array = [0, 1]\n        solution.move_zeroes(array)\n        self.assertEqual(array, [1, 0])\n        array = [0]\n        solution.move_zeroes(array)\n        self.assertEqual(array, [0])\n        array = [1]\n        solution.move_zeroes(array)\n        self.assertEqual(array, [1])\n        array = [1, 1]\n        solution.move_zeroes(array)\n        self.assertEqual(array, [1, 1])\n        print('Success: test_move_zeroes')\n\n\ndef main():\n    test = TestMoveZeroes()\n    test.test_move_zeroes()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_move_zeroes.py')

