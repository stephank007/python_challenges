#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Create a class with an insert method to insert an int to a list.  It should also support calculating the max, min, mean, and mode in O(1).
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume the inputs are valid?
#     * No
# * Is there a range of inputs?
#     * 0 <= item <= 100
# * Should mean return a float?
#     * Yes
# * Should the other results return an int?
#     * Yes
# * If there are multiple modes, what do we return?
#     * Any of the modes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * [] -> ValueError
# * [5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
#     * max: 9
#     * min: 2
#     * mean: 55
#     * mode: 9 or 2

# ## Algorithm
# 
# Return the input, val
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


from __future__ import division


class Solution(object):

    def __init__(self, upper_limit=100):
        self.max = None
        self.min = None
        # Mean
        self.num_items = 0
        self.running_sum = 0
        self.mean = None
        # Mode
        self.array = [0] * (upper_limit+1)
        self.mode_ocurrences = 0
        self.mode = None

    def insert(self, val):
        if val is None:
            raise TypeError('val cannot be None')
        if self.max is None or val > self.max:
            self.max = val
        if self.min is None or val < self.min:
            self.min = val
        # Calculate the mean
        self.num_items += 1
        self.running_sum += val
        self.mean = self.running_sum / self.num_items
        # Calculate the mode
        self.array[val] += 1
        if self.array[val] > self.mode_ocurrences:
            self.mode_ocurrences = self.array[val]
            self.mode = val


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_math_ops.py', "import unittest\n\n\nclass TestMathOps(unittest.TestCase):\n\n    def test_math_ops(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.insert, None)\n        solution.insert(5)\n        solution.insert(2)\n        solution.insert(7)\n        solution.insert(9)\n        solution.insert(9)\n        solution.insert(2)\n        solution.insert(9)\n        solution.insert(4)\n        solution.insert(3)\n        solution.insert(3)\n        solution.insert(2)\n        self.assertEqual(solution.max, 9)\n        self.assertEqual(solution.min, 2)\n        self.assertEqual(solution.mean, 5)\n        self.assertTrue(solution.mode in (2, 9))\n        print('Success: test_math_ops')\n\n\ndef main():\n    test = TestMathOps()\n    test.test_math_ops()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_math_ops.py')

