#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a stack with push, pop, and min methods running O(1) time.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume this is a stack of ints?
#     * Yes
# * Can we assume the input values for push are valid?
#     * Yes
# * If we call this function on an empty stack, can we return sys.maxsize?
#     * Yes
# * Can we assume we already have a stack class that can be used for this problem?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * Push/pop on empty stack
# * Push/pop on non-empty stack
# * Min on empty stack
# * Min on non-empty stack

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack_min/stack_min_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../stack/stack.py')
get_ipython().run_line_magic('load', '../stack/stack.py')


# In[ ]:


import sys


class StackMin(Stack):

    def __init__(self, top=None):
        # TODO: Implement me
        pass

    def minimum(self):
        # TODO: Implement me
        pass

    def push(self, data):
        # TODO: Implement me
        pass

    def pop(self):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_stack_min.py
import unittest


class TestStackMin(unittest.TestCase):

    def test_stack_min(self):
        print('Test: Push on empty stack, non-empty stack')
        stack = StackMin()
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.minimum(), 5)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.minimum(), 1)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.minimum(), 1)
        stack.push(0)
        self.assertEqual(stack.peek(), 0)
        self.assertEqual(stack.minimum(), 0)

        print('Test: Pop on non-empty stack')
        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.minimum(), 1)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.minimum(), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.minimum(), 5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.minimum(), sys.maxsize)

        print('Test: Pop empty stack')
        self.assertEqual(stack.pop(), None)

        print('Success: test_stack_min')


def main():
    test = TestStackMin()
    test.test_stack_min()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack_min/stack_min_solution.ipynb) for a discussion on algorithms and code solutions.
