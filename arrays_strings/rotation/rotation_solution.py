#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the string is ASCII?
#     * Yes
#     * Note: Unicode strings could require special handling depending on your language
# * Is this case sensitive?
#     * Yes
# * Can we use additional data structures?  
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * Any strings that differ in size -> False
# * None, 'foo' -> False (any None results in False)
# * ' ', 'foo' -> False
# * ' ', ' ' -> True
# * 'foobarbaz', 'barbazfoo' -> True

# ## Algorithm
# 
# Examine the following test case:
# * s1 = 'barbazfoo'
# * s2 = 'foobarbaz'
# 
# We see that if we can use the given is_substring method if we take compare s2 with s1 + s1:
# * s2 = 'foobarbaz'
# * s3 = 'barbaz*foobarbaz*foo'
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Code

# In[1]:


class Rotation(object):

    def is_substring(self, s1, s2):
        return s1 in s2

    def is_rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        return self.is_substring(s1, s2 + s2)


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_rotation.py', "import unittest\n\n\nclass TestRotation(unittest.TestCase):\n\n    def test_rotation(self):\n        rotation = Rotation()\n        self.assertEqual(rotation.is_rotation('o', 'oo'), False)\n        self.assertEqual(rotation.is_rotation(None, 'foo'), False)\n        self.assertEqual(rotation.is_rotation('', 'foo'), False)\n        self.assertEqual(rotation.is_rotation('', ''), True)\n        self.assertEqual(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)\n        print('Success: test_rotation')\n\n\ndef main():\n    test = TestRotation()\n    test.test_rotation()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_rotation.py')

