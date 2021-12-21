#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a stack with push, pop, peek, and is_empty methods using a linked list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Pythonic-Code](#Pythonic-Code)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * If we pop on an empty stack, do we return None?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# ### Push
# 
# * Push to empty stack
# * Push to non-empty stack
# 
# ### Pop
# 
# * Pop on empty stack
# * Pop on single element stack
# * Pop on multiple element stack
# 
# ### Peek
# 
# * Peek on empty stack
# * Peek on one or more element stack
# 
# ### Is Empty
# 
# * Is empty on empty stack
# * Is empty on one or more element stack

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack/stack_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Node(object):

    def __init__(self, data):
        # TODO: Implement me
        pass


class Stack(object):

    def __init__(self, top=None):
        # TODO: Implement me
        pass

    def push(self, data):
        # TODO: Implement me
        pass

    def pop(self):
        # TODO: Implement me
        pass

    def peek(self):
        # TODO: Implement me
        pass

    def is_empty(self):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_stack.py
import unittest


class TestStack(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Empty stack')
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.pop(), None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.is_empty(), True)

        print('Success: test_end_to_end')


def main():
    test = TestStack()
    test.test_end_to_end()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack/stack_solution.ipynb) for a discussion on algorithms and code solutions.
