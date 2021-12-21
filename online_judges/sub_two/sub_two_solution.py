#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Sum of Two Integers (Subtraction Variant).
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
# * 7, 5 -> 2
# * -5, -7 -> 2
# * -5, 7 -> -12
# * 5, -7 -> 12
# </pre>

# ## Algorithm
# 
# We'll look at the following example, subtracting a and b:
# 
# <pre>
# a 0110 = 6 
# b 0101 = 5
# </pre>
# 
# First, subtract a and b, without worrying about the borrow (0-0=0, 0-1=1, 1-1=0):
# 
# result = a ^ b = 0011
# 
# Next, calculate the borrow (0-1=1).  We'll need to left shift one to prepare for the next iteration when we move to the next most significant bit:
# 
# ~a     = 1001
#  b     = 0101
# ~a & b = 0001
# 
# borrow = (~a&b) << 1 = 0010
# 
# If the borrow is not zero, we'll need to subtract the borrow from the result.  Recursively call the function, passing in result and borrow.
# 
# Complexity:
# * Time: O(b), where b is the number of bits
# * Space: O(b), where b is the number of bits

# ## Code

# In[1]:


class Solution(object):

    def sub_two(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b;
        borrow = (~a&b) << 1
        if borrow != 0:
            return self.sub_two(result, borrow)
        return result;


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_sub_two.py', "import unittest\n\n\nclass TestSubTwo(unittest.TestCase):\n\n    def test_sub_two(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.sub_two, None)\n        self.assertEqual(solution.sub_two(7, 5), 2)\n        self.assertEqual(solution.sub_two(-5, -7), 2)\n        self.assertEqual(solution.sub_two(-5, 7), -12)\n        self.assertEqual(solution.sub_two(5, -7), 12)\n        print('Success: test_sub_two')\n\n\ndef main():\n    test = TestSubTwo()\n    test.test_sub_two()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_sub_two.py')

