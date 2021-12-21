#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement n stacks using a single array.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Are the stacks and array a fixed size?
#     * Yes
# * Are the stacks equally sized?
#     * Yes
# * Does pushing to a full stack result in an exception?
#     * Yes
# * Does popping from an empty stack result in an exception?
#     * Yes
# * Can we assume the user passed in stack index is valid?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * Test the following on the three stacks:
#     * Push to full stack -> Exception
#     * Push to non-full stack
#     * Pop on empty stack -> Exception
#     * Pop on non-empty stack

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/n_stacks/n_stacks_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        # TODO: Implement me
        pass

    def abs_index(self, stack_index):
        # TODO: Implement me
        pass

    def push(self, stack_index, data):
        # TODO: Implement me
        pass

    def pop(self, stack_index):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_n_stacks.py
import unittest


class TestStacks(unittest.TestCase):

    def test_pop_on_empty(self, num_stacks, stack_size):
        print('Test: Pop on empty stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.pop(0)

    def test_push_on_full(self, num_stacks, stack_size):
        print('Test: Push to full stack')
        stacks = Stacks(num_stacks, stack_size)
        for i in range(0, stack_size):
            stacks.push(2, i)
        stacks.push(2, stack_size)

    def test_stacks(self, num_stacks, stack_size):
        print('Test: Push to non-full stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')
        self.assertEqual(stacks.pop(0), 2)
        self.assertEqual(stacks.pop(0), 1)
        self.assertEqual(stacks.pop(1), 3)
        self.assertEqual(stacks.pop(2), 4)

        print('Success: test_stacks\n')


def main():
    num_stacks = 3
    stack_size = 100
    test = TestStacks()
    test.assertRaises(Exception, test.test_pop_on_empty, num_stacks,
                      stack_size)
    test.assertRaises(Exception, test.test_push_on_full, num_stacks,
                      stack_size)
    test.test_stacks(num_stacks, stack_size)


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/n_stacks/n_stacks_solution.ipynb) for a discussion on algorithms and code solutions.
