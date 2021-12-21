#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Determine if a string is a permutation of another string.
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
# * Is whitespace important?
#     * Yes
# * Is this case sensitive?  'Nib', 'bin' is not a match?
#     * Yes
# * Can we use additional data structures?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * One or more None inputs -> False
# * One or more empty strings -> False
# * 'Nib', 'bin' -> False
# * 'act', 'cat' -> True
# * 'a ct', 'ca t' -> True

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/permutation/permutation_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Permutations(object):

    def is_permutation(self, str1, str2):
        # TODO: Implement me
        pass


# ## Unit Test

# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_permutation_solution.py
import unittest


class TestPermutation(unittest.TestCase):

    def test_permutation(self, func):
        self.assertEqual(func(None, 'foo'), False)
        self.assertEqual(func('', 'foo'), False)
        self.assertEqual(func('Nib', 'bin'), False)
        self.assertEqual(func('act', 'cat'), True)
        self.assertEqual(func('a ct', 'ca t'), True)
        self.assertEqual(func('dog', 'doggo'), False)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)
    try:
        permutations_alt = PermutationsAlt()
        test.test_permutation(permutations_alt.is_permutation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/permutation/permutation_solution.ipynb) for a discussion on algorithms and code solutions.
