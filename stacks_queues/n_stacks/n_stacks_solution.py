#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement n stacks using a single array.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# ### Absolute Index
# 
# * return stack size * stack index + stack pointer
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Push
# 
# * If stack is full, throw exception
# * Else
#     * Increment stack pointer
#     * Get the absolute array index
#     * Insert the value to this index
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Pop
# 
# * If stack is empty, throw exception
# * Else
#     * Store the value contained in the absolute array index
#     * Set the value in the absolute array index to None
#     * Decrement stack pointer
#     * return value
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stacks
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]

    def push(self, stack_index, data):
        if self.stack_pointers[stack_index] == self.stack_size - 1:
            raise Exception('Stack is full')
        self.stack_pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data

    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise Exception('Stack is empty')
        array_index = self.abs_index(stack_index)
        data = self.stack_array[array_index]
        self.stack_array[array_index] = None
        self.stack_pointers[stack_index] -= 1
        return data


# ## Unit Test
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_n_stacks.py', "import unittest\n\n\nclass TestStacks(unittest.TestCase):\n\n    def test_pop_on_empty(self, num_stacks, stack_size):\n        print('Test: Pop on empty stack')\n        stacks = Stacks(num_stacks, stack_size)\n        stacks.pop(0)\n\n    def test_push_on_full(self, num_stacks, stack_size):\n        print('Test: Push to full stack')\n        stacks = Stacks(num_stacks, stack_size)\n        for i in range(0, stack_size):\n            stacks.push(2, i)\n        stacks.push(2, stack_size)\n\n    def test_stacks(self, num_stacks, stack_size):\n        print('Test: Push to non-full stack')\n        stacks = Stacks(num_stacks, stack_size)\n        stacks.push(0, 1)\n        stacks.push(0, 2)\n        stacks.push(1, 3)\n        stacks.push(2, 4)\n\n        print('Test: Pop on non-empty stack')\n        self.assertEqual(stacks.pop(0), 2)\n        self.assertEqual(stacks.pop(0), 1)\n        self.assertEqual(stacks.pop(1), 3)\n        self.assertEqual(stacks.pop(2), 4)\n\n        print('Success: test_stacks\\n')\n\n\ndef main():\n    num_stacks = 3\n    stack_size = 100\n    test = TestStacks()\n    test.assertRaises(Exception, test.test_pop_on_empty, num_stacks,\n                      stack_size)\n    test.assertRaises(Exception, test.test_push_on_full, num_stacks,\n                      stack_size)\n    test.test_stacks(num_stacks, stack_size)\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


run -i test_n_stacks.py


# In[ ]:




