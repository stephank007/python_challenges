#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine if a number is a power of two.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the input number an int?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Is the output a boolean?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * 0 -> False
# * 1 -> True
# * 2 -> True
# * 15 -> False
# * 16 -> True

# ## Algorithm
# 
# We can use bit manipulation to determine if a number is a power of two.  
# 
# For a number to be a power of two, there must only be one bit that is a `1`.  
# 
# We can use the following bit manipulation trick to determine this:
# 
# `n & (n - 1)`
# 
# Here's an example why:
# 
# <pre>
# 0000 1000 = n
# 0000 0001 = 1
# 0000 0111 = n-1
# 
# 0000 1000 = n
# 0000 0111 = n-1
# 0000 0000 = n & n-1, result = 0
# </pre>
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def is_power_of_two(self, n):
        if n is None:
            raise TypeError('n cannot be None')
        if n <= 0:
            return False
        return (n & (n - 1)) == 0


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_is_power_of_two.py', "import unittest\n\n\nclass TestSolution(unittest.TestCase):\n\n    def test_is_power_of_two(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.is_power_of_two, None)\n        self.assertEqual(solution.is_power_of_two(0), False)\n        self.assertEqual(solution.is_power_of_two(1), True)\n        self.assertEqual(solution.is_power_of_two(2), True)\n        self.assertEqual(solution.is_power_of_two(15), False)\n        self.assertEqual(solution.is_power_of_two(16), True)\n        print('Success: test_is_power_of_two')\n\n\ndef main():\n    test = TestSolution()\n    test.test_is_power_of_two()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_is_power_of_two.py')

