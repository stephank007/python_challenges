#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Check if a number is prime.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is it correct that 1 is not considered a prime number?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * Not an int -> Exception
# * Less than 2 -> False
# * General case

# ## Algorithm
# 
# For a number to be prime, it must be 2 or greater and cannot be divisible by another number other than itself (and 1).
# 
# We'll check by dividing all numbers from 2 to the input number to determine if the number is prime.
# 
# As an optimization, we can divide from 2 to the square root of the input number.  For each value that divides the input number evenly, there is a complement b where a * b = n.  If a > sqrt(n) then b < sqrt(n) because sqrt(n^2) = n.
# 
# Complexity:
# * Time: O(n) where n is the value of the input number
# * Space: O(1)
# 
# ### Sieve of Eratosthenes
# 
# The Sieve of Eratosthenes provides a more efficient way of computing and generating primes.  See the challenge ["Generate a list of primes"]() for more details.

# ## Code

# In[1]:


import math


class Math(object):

    def check_prime(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def check_prime_optimized(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_check_prime.py', "import unittest\n\n\nclass TestMath(unittest.TestCase):\n\n    def test_check_prime(self):\n        math = Math()\n        self.assertRaises(TypeError, math.check_prime, None)\n        self.assertRaises(TypeError, math.check_prime, 98.6)\n        self.assertEqual(math.check_prime(0), False)\n        self.assertEqual(math.check_prime(1), False)\n        self.assertEqual(math.check_prime(97), True)\n        print('Success: test_check_prime')\n\n\ndef main():\n    test = TestMath()\n    test.test_check_prime()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_check_prime.py')

