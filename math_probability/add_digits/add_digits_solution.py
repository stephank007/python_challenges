#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given an int, repeatedly add its digits until the result is one digit.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume num is not negative?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None input -> TypeError
# * negative input -> ValueError
# * 9 -> 9
# * 138 -> 3
# * 65536 -> 7
# </pre>

# ## Algorithm
# 
# The naive solution simply isolates each digit with with modulo and integer division.  We'll add each isolated digit to  a list and sum the values.
# 
# <pre>
# 138 % 10 = 8 -> isolated
# 138 // 10 = 13
# 13 % 10 = 3 -> isolated
# 13 // 10 = 1
# 1 % 10 = 1 -> isolated
# </pre>
# 
# A more optimal solution exists, by recognizing this is a digital root.  See the [Wikipedia article](https://en.wikipedia.org/wiki/Digital_root) for more information.
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def add_digits(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 0:
            raise ValueError('num cannot be negative')
        digits = []
        while num != 0:
            digits.append(num % 10)
            num //= 10
        digits_sum = sum(digits)
        if digits_sum >= 10:
            return self.add_digits(digits_sum)
        else:
            return digits_sum

    def add_digits_optimized(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 0:
            raise ValueError('num cannot be negative')
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_add_digits.py', "import unittest\n\n\nclass TestAddDigits(unittest.TestCase):\n\n    def test_add_digits(self, func):\n        self.assertRaises(TypeError, func, None)\n        self.assertRaises(ValueError, func, -1)\n        self.assertEqual(func(0), 0)\n        self.assertEqual(func(9), 9)\n        self.assertEqual(func(138), 3)\n        self.assertEqual(func(65536), 7) \n        print('Success: test_add_digits')\n\n\ndef main():\n    test = TestAddDigits()\n    solution = Solution()\n    test.test_add_digits(solution.add_digits)\n    try:\n        test.test_add_digits(solution.add_digits_optimized)\n    except NameError:\n        # Alternate solutions are only defined\n        # in the solutions file\n        pass\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_add_digits.py')

