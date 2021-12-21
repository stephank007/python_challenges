#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a stack with push, pop, and min methods running O(1) time.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# We'll use a second stack to keep track of the minimum values.
# 
# ### Min
# 
# * If the second stack is empty, return an error code (max int value)
# * Else, return the top of the stack, without popping it
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Push
# 
# * Push the data
# * If the data is less than min
#     * Push data to second stack
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Pop
# 
# * Pop the data
# * If the data is equal to min
#     * Pop the top of the second stack
# * Return the data
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../stack/stack.py')


# In[2]:


import sys


class StackMin(Stack):

    def __init__(self, top=None):
        super(StackMin, self).__init__(top)
        self.stack_of_mins = Stack()

    def minimum(self):
        if self.stack_of_mins.top is None:
            return sys.maxsize
        else:
            return self.stack_of_mins.peek()

    def push(self, data):
        super(StackMin, self).push(data)
        if data < self.minimum():
            self.stack_of_mins.push(data)

    def pop(self):
        data = super(StackMin, self).pop()
        if data == self.minimum():
            self.stack_of_mins.pop()
        return data


# ## Unit Test
# 
# 

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_stack_min.py', "import unittest\n\n\nclass TestStackMin(unittest.TestCase):\n\n    def test_stack_min(self):\n        print('Test: Push on empty stack, non-empty stack')\n        stack = StackMin()\n        stack.push(5)\n        self.assertEqual(stack.peek(), 5)\n        self.assertEqual(stack.minimum(), 5)\n        stack.push(1)\n        self.assertEqual(stack.peek(), 1)\n        self.assertEqual(stack.minimum(), 1)\n        stack.push(3)\n        self.assertEqual(stack.peek(), 3)\n        self.assertEqual(stack.minimum(), 1)\n        stack.push(0)\n        self.assertEqual(stack.peek(), 0)\n        self.assertEqual(stack.minimum(), 0)\n\n        print('Test: Pop on non-empty stack')\n        self.assertEqual(stack.pop(), 0)\n        self.assertEqual(stack.minimum(), 1)\n        self.assertEqual(stack.pop(), 3)\n        self.assertEqual(stack.minimum(), 1)\n        self.assertEqual(stack.pop(), 1)\n        self.assertEqual(stack.minimum(), 5)\n        self.assertEqual(stack.pop(), 5)\n        self.assertEqual(stack.minimum(), sys.maxsize)\n\n        print('Test: Pop empty stack')\n        self.assertEqual(stack.pop(), None)\n\n        print('Success: test_stack_min')\n\n\ndef main():\n    test = TestStackMin()\n    test.test_stack_min()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


run -i test_stack_min.py

