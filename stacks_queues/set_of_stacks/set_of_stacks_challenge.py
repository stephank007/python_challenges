#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement SetOfStacks that wraps a list of stacks, where each stack is bound by a capacity.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume we already have a stack class that can be used for this problem?
#     * Yes
# * Are all stack bound by the same capacity?
#     * Yes
# * If a stack becomes full, should automatically create one?
#     * Yes
# * If a stack becomes empty, should we delete it?
#     * Yes
# * If we pop on an empty stack, should we return None?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * Push and pop on an empty stack
# * Push and pop on a non-empty stack
# * Push on a capacity stack to create a new one
# * Pop on a stack to destroy it

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/set_of_stacks/set_of_stacks_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../stack/stack.py')
get_ipython().run_line_magic('load', '../stack/stack.py')


# In[ ]:


class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        # TODO: Implement me
        pass

    def push(self, data):
        # TODO: Implement me
        pass

    def pop(self):
        # TODO: Implement me
        pass

    def is_full(self):
        # TODO: Implement me
        pass


class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
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


# %load test_set_of_stacks.py
import unittest


class TestSetOfStacks(unittest.TestCase):

    def test_set_of_stacks(self):
        print('Test: Push on an empty stack')
        stacks = SetOfStacks(indiv_stack_capacity=2)
        stacks.push(3)

        print('Test: Push on a non-empty stack')
        stacks.push(5)

        print('Test: Push on a capacity stack to create a new one')
        stacks.push('a')

        print('Test: Pop on a stack to destroy it')
        self.assertEqual(stacks.pop(), 'a')

        print('Test: Pop general case')
        self.assertEqual(stacks.pop(), 5)
        self.assertEqual(stacks.pop(), 3)

        print('Test: Pop on no elements')
        self.assertEqual(stacks.pop(), None)

        print('Success: test_set_of_stacks')


def main():
    test = TestSetOfStacks()
    test.test_set_of_stacks()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/set_of_stacks/set_of_stacks_solution.ipynb) for a discussion on algorithms and code solutions.
