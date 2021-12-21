#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement SetOfStacks that wraps a list of stacks, where each stack is bound by a capacity.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# ### Push
# 
# * If there are no stacks or the last stack is full
#     * Create a new stack
# * Push to the new stack
# 
# Complexity:
# * Time: O(1)
# * Space: O(m), where m is the size of the new stack if the last stack is full
# 
# ### Pop
# 
# * If there are no stacks, return None
# * Else if the last stack has one element
#     * Pop the last element's data
#     * Delete the now empty stack
#     * Update the last stack pointer
# * Else Pop the last element's data
# * Return the last element's data
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../stack/stack.py')


# In[2]:


class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        super(StackWithCapacity, self).__init__(top)
        self.capacity = capacity
        self.num_items = 0

    def push(self, data):
        if self.is_full():
            raise Exception('Stack full')
        super(StackWithCapacity, self).push(data)
        self.num_items += 1

    def pop(self):
        self.num_items -= 1
        return super(StackWithCapacity, self).pop()

    def is_full(self):
        return self.num_items == self.capacity

    def is_empty(self):
        return self.num_items == 0


class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
        self.indiv_stack_capacity = indiv_stack_capacity
        self.stacks = []
        self.last_stack = None

    def push(self, data):
        if self.last_stack is None or self.last_stack.is_full():
            self.last_stack = StackWithCapacity(None, self.indiv_stack_capacity)
            self.stacks.append(self.last_stack)
        self.last_stack.push(data)

    def pop(self):
        if self.last_stack is None:
            return None
        data = self.last_stack.pop()
        if self.last_stack.is_empty():
            self.stacks.pop()
            self.last_stack = self.stacks[-1] if self.stacks else None
        return data


# ## Unit Test
# 
# 

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_set_of_stacks.py', "import unittest\n\n\nclass TestSetOfStacks(unittest.TestCase):\n\n    def test_set_of_stacks(self):\n        print('Test: Push on an empty stack')\n        stacks = SetOfStacks(indiv_stack_capacity=2)\n        stacks.push(3)\n\n        print('Test: Push on a non-empty stack')\n        stacks.push(5)\n\n        print('Test: Push on a capacity stack to create a new one')\n        stacks.push('a')\n\n        print('Test: Pop on a stack to destroy it')\n        self.assertEqual(stacks.pop(), 'a')\n\n        print('Test: Pop general case')\n        self.assertEqual(stacks.pop(), 5)\n        self.assertEqual(stacks.pop(), 3)\n\n        print('Test: Pop on no elements')\n        self.assertEqual(stacks.pop(), None)\n\n        print('Success: test_set_of_stacks')\n\n\ndef main():\n    test = TestSetOfStacks()\n    test.test_set_of_stacks()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_set_of_stacks.py')

