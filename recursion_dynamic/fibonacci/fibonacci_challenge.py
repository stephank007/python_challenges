#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement fibonacci recursively, dynamically, and iteratively.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Does the sequence start at 0 or 1?
#     * 0
# * Can we assume the inputs are valid non-negative ints?
#     * Yes
# * Are you looking for a recursive or iterative solution?
#     * Implement both
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
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/fibonacci/fibonacci_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Math(object):

    def fib_iterative(self, n):
        # TODO: Implement me
        pass

    def fib_recursive(self, n):
        # TODO: Implement me
        pass

    def fib_dynamic(self, n):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_fibonacci.py
import unittest


class TestFib(unittest.TestCase):

    def test_fib(self, func):
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        self.assertEqual(result, expected)
        print('Success: test_fib')


def main():
    test = TestFib()
    math = Math()
    test.test_fib(math.fib_recursive)
    test.test_fib(math.fib_dynamic)
    test.test_fib(math.fib_iterative)


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/fibonacci/fibonacci_solution.ipynb) for a discussion on algorithms and code solutions.
