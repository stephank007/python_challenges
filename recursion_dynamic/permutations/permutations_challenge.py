#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find all permutations of an input string.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can the input have duplicates?
#     * Yes
# * Can the output have duplicates?
#     * No
# * Is the output a list of strings?
#     * Yes
# * Do we have to output the results in sorted order?
#     * No
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> None
# * '' -> ''
# * 'AABC' -> ['AABC', 'AACB', 'ABAC', 'ABCA',
#              'ACAB', 'ACBA', 'BAAC', 'BACA',
#              'BCAA', 'CAAB', 'CABA', 'CBAA']
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Permutations(object):

    def find_permutations(self, string):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_permutations.py
import unittest


class TestPermutations(unittest.TestCase):

    def test_permutations(self):
        permutations = Permutations()
        self.assertEqual(permutations.find_permutations(None), None)
        self.assertEqual(permutations.find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        self.assertEqual(permutations.find_permutations(string), expected)
        print('Success: test_permutations')


def main():
    test = TestPermutations()
    test.test_permutations()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
