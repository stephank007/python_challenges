#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the highest product of three numbers in a list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the input a list of integers?
#     * Yes
# * Can we get negative inputs?
#     * Yes
# * Can there be duplicate entries in the input?
#     * Yes
# * Will there always be at least three integers?
#     * No
# * Can we assume the inputs are valid?
#     * No, check for None input
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * Less than three ints -> ValueError
# * [5, -2, 3] -> -30
# * [5, -2, 3, 1, -1, 4] -> 60

# ## Algorithm
# 
# ### Brute force:
# 
# Use three loops and multiple each numbers.
# 
# Complexity:
# * Time: O(n^3)
# * Space: O(1)
# 
# ### Sorting:
# 
# Sort the list, multiply the last three elements.
# 
# Complexity:
# * Time: O(n log(n))
# * Space: O(1)
# 
# ### Greedy:
# 
# <pre>
#  0   1  2  3   4  5
# [5, -2, 3, 1, -1, 4] -> 60
# 
# max_prod_of_three = -30
# max_prod_of_two = -10
# max_num = 5
# min_prod_of_two = -10
# min_num = -2
# 
#  0   1  2  3   4  5
# [5, -2, 3, 1, -1, 4] -> 60
#         ^
# max_prod_of_three = -30
# max_prod_of_two = 15
# max_num = 5
# min_prod_of_two = -10
# min_num = -2
# 
#  0   1  2  3   4  5
# [5, -2, 3, 1, -1, 4] -> 60
#            ^
# max_prod_of_three = 15
# max_prod_of_two = 15
# max_num = 5
# min_prod_of_two = -10
# min_num = -2
# 
#  0   1  2  3   4  5
# [5, -2, 3, 1, -1, 4] -> 60
#                ^
# max_prod_of_three = 15
# max_prod_of_two = 15
# max_num = 5
# min_prod_of_two = -10
# min_num = -2
# 
#  0   1  2  3   4  5
# [5, -2, 3, 1, -1, 4] -> 60
#                   ^
# max_prod_of_three = 60
# max_prod_of_two = 15
# max_num = 5
# min_prod_of_two = -10
# min_num = -2
# </pre>
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def max_prod_three_nlogn(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if len(array) < 3:
            raise ValueError('array must have 3 or more ints')
        array.sort()
        product = 1
        for item in array[-3:]:
            product *= item
        return product

    def max_prod_three(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if len(array) < 3:
            raise ValueError('array must have 3 or more ints')
        curr_max_prod_three = array[0] * array[1] * array[2]
        max_prod_two = array[0] * array[1]
        min_prod_two = array[0] * array[1]
        max_num = max(array[0], array[1])
        min_num = min(array[0], array[1])
        for i in range(2, len(array)):
            curr_max_prod_three = max(curr_max_prod_three,
                                      max_prod_two * array[i],
                                      min_prod_two * array[i])
            max_prod_two = max(max_prod_two,
                               max_num * array[i],
                               min_num * array[i])
            min_prod_two = min(min_prod_two,
                               max_num * array[i],
                               min_num * array[i])
            max_num = max(max_num, array[i])
            min_num = min(min_num, array[i])
        return curr_max_prod_three


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_prod_three.py', "import unittest\n\n\nclass TestProdThree(unittest.TestCase):\n\n    def test_prod_three(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.max_prod_three, None)\n        self.assertRaises(ValueError, solution.max_prod_three, [1, 2])\n        self.assertEqual(solution.max_prod_three([5, -2, 3]), -30)\n        self.assertEqual(solution.max_prod_three([5, -2, 3, 1, -1, 4]), 60)\n        print('Success: test_prod_three')\n\n\ndef main():\n    test = TestProdThree()\n    test.test_prod_three()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_prod_three.py')

