#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement fibonacci recursively, dynamically, and iteratively.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Does the sequence start at 0 or 1?
#     * 0
# * Can we assume the inputs are valid non-negative ints?
#     * Yes
# * Are you looking for a recursive or iterative solution?
#     * Either
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * n = 0 -> 0
# * n = 1 -> 1
# * n = 6 -> 8
# * Fib sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

# ## Algorithm
# 
# Recursive:
# * Fibonacci is as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# * If n = 0 or 1, return n
# * Else return fib(n-1) + fib(n-2)
# 
# Complexity:
# * Time: O(2^n) if recursive or iterative, O(n) if dynamic
# * Space: O(n) if recursive, O(1) if iterative, O(n) if dynamic

# ## Code

# In[1]:


class Math(object):

    def fib_iterative(self, n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def fib_recursive(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_dynamic(self, n):
        cache = {}
        return self._fib_dynamic(n, cache)

    def _fib_dynamic(self, n, cache):
        if n == 0 or n == 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self._fib_dynamic(n-1, cache) + self._fib_dynamic(n-2, cache)
        return cache[n]


# ## Unit Test
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_fibonacci.py', "import unittest\n\n\nclass TestFib(unittest.TestCase):\n\n    def test_fib(self, func):\n        result = []\n        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n        for i in range(len(expected)):\n            result.append(func(i))\n        self.assertEqual(result, expected)\n        print('Success: test_fib')\n\n\ndef main():\n    test = TestFib()\n    math = Math()\n    test.test_fib(math.fib_recursive)\n    test.test_fib(math.fib_dynamic)\n    test.test_fib(math.fib_iterative)\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_fibonacci.py')

