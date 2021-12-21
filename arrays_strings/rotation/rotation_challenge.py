#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

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
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/rotation/rotation_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Rotation(object):

    def is_substring(self, s1, s2):
        # TODO: Implement me
        pass

    def is_rotation(self, s1, s2):
        # TODO: Implement me
        # Call is_substring only once
        pass


# ## Unit Test

# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_rotation.py
import unittest


class TestRotation(unittest.TestCase):

    def test_rotation(self):
        rotation = Rotation()
        self.assertEqual(rotation.is_rotation('o', 'oo'), False)
        self.assertEqual(rotation.is_rotation(None, 'foo'), False)
        self.assertEqual(rotation.is_rotation('', 'foo'), False)
        self.assertEqual(rotation.is_rotation('', ''), True)
        self.assertEqual(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/rotation/rotation_solution.ipynb) for a discussion on algorithms and code solutions.
