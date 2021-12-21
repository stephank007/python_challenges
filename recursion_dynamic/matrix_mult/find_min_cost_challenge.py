#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a list of 2x2 matrices, minimize the cost of matrix multiplication.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Do we just want to calculate the cost and not list the actual order of operations?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * [] -> 0
# * [Matrix(2, 3), Matrix(3, 6), Matrix(6, 4), Matrix(4, 5)] -> 124

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Matrix(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second


# In[ ]:


class MatrixMultiplicationCost(object):

    def find_min_cost(self, matrices):
    # TODO: Implement me
    pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_find_min_cost.py
import unittest


class TestMatrixMultiplicationCost(unittest.TestCase):

    def test_find_min_cost(self):
        matrix_mult_cost = MatrixMultiplicationCost()
        self.assertRaises(TypeError, matrix_mult_cost.find_min_cost, None)
        self.assertEqual(matrix_mult_cost.find_min_cost([]), 0)
        matrices = [Matrix(2, 3),
                    Matrix(3, 6),
                    Matrix(6, 4),
                    Matrix(4, 5)]
        expected_cost = 124
        self.assertEqual(matrix_mult_cost.find_min_cost(matrices), expected_cost)
        print('Success: test_find_min_cost')


def main():
    test = TestMatrixMultiplicationCost()
    test.test_find_min_cost()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
