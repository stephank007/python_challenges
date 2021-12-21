#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Sum of Two Integers.
# 
# See the [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) problem page.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume we're working with 32 bit ints?
#     * Yes
# * Can we assume the inputs are valid?
#     * No, check for None
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None input -> TypeError
# * 5, 7 -> 12
# * -5, -7 -> -12
# * 5, -7 -> -2
# </pre>

# ## Algorithm
# 
# We'll look at the following example, adding a and b:
# 
# <pre>
# a 0111 
# b 0101
# </pre>
# 
# First, add a and b, without worrying about the carry (0+0=0, 0+1=1, 1+1=0):
# 
# result = a ^ b = 0010
# 
# Next, calculate the carry (1+1=2).  We'll need to left shift one to prepare for the next iteration when we move to the next most significant bit:
# 
# carry = (a&b) << 1 = 1010
# 
# If the carry is not zero, we'll need to add the carry to the result.  Recursively call the function, passing in result and carry.
# 
# Below are the values of a, b, and the carry of a = 7 and b = 5, producing the result of 12.
# 
# <pre>
# a 0111 
# b 0101 
# ----- 
# c 0101 
# a 0010 
# b 1010 
# ----- 
# c 0010 
# a 1000 
# b 0100 
# ----- 
# c 0000 
# a 1100 
# b 0000
# 
# c = carry = 0, return the result 1100
# </pre>
# 
# Complexity:
# * Time: O(b), where b is the number of bits
# * Space: O(b), where b is the number of bits

# ## Code

# In[1]:


class Solution(object):

    def sum_two(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b;
        carry = (a&b) << 1
        if carry != 0:
            return self.sum_two(result, carry)
        return result;


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_sum_two.py', "import unittest\n\n\nclass TestSumTwo(unittest.TestCase):\n\n    def test_sum_two(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.sum_two, None)\n        self.assertEqual(solution.sum_two(5, 7), 12)\n        self.assertEqual(solution.sum_two(-5, -7), -12)\n        self.assertEqual(solution.sum_two(5, -7), -2)\n        print('Success: test_sum_two')\n\n\ndef main():\n    test = TestSumTwo()\n    test.test_sum_two()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_sum_two.py')

