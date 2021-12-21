#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Author](https://github.com/). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement foo(val), which returns val
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Does foo do anything else?
#     * No

# ## Test Cases
# 
# * foo(val) -> val

# ## Algorithm
# 
# Return the input, val
#     
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


def foo(val):
    return val


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_foo.py', "import unittest\n\n\nclass TestFoo(unittest.TestCase):\n\n    def test_foo(self):\n        self.assertEqual(foo(None), None)\n        self.assertEqual(foo(0), 0)\n        self.assertEqual(foo('bar'), 'bar')\n        print('Success: test_foo')\n\n\ndef main():\n    test = TestFoo()\n    test.test_foo()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_foo.py')

