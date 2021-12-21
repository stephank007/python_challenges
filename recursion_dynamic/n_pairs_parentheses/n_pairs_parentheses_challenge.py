#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Rishi Rajasekaran](https://github.com/rishihot55). Source and license info is available on [Github](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find all valid combinations of n-pairs of parentheses.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the input an integer representing the number of pairs?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Is the output a list of valid combinations?
#     * Yes
# * Should the output have duplicates?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> Exception
# * Negative -> Exception
# * 0 -> []
# * 1 -> ['()']
# * 2 -> ['(())', '()()']
# * 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/n_pairs_parentheses/n_pairs_parentheses_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Parentheses(object):

    def find_pair(self, num_pairs):
        # TODO: implement me
        pass


# ## Unit Test

# In[ ]:


# %load test_n_pairs_parentheses.py
import unittest


class TestPairParentheses(unittest.TestCase):

    def test_pair_parentheses(self):
        parentheses = Parentheses()
        self.assertRaises(TypeError, parentheses.find_pair, None)
        self.assertRaises(ValueError, parentheses.find_pair, -1)
        self.assertEqual(parentheses.find_pair(0), [])
        self.assertEqual(parentheses.find_pair(1), ['()'])
        self.assertEqual(parentheses.find_pair(2), ['(())',
                                                '()()'])
        self.assertEqual(parentheses.find_pair(3), ['((()))',
                                                '(()())',
                                                '(())()',
                                                '()(())',
                                                '()()()'])
        print('Success: test_pair_parentheses')


def main():
    test = TestPairParentheses()
    test.test_pair_parentheses()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/n_pairs_parentheses/n_pairs_parentheses_solution.ipynb) for a discussion on algorithms and code solutions.
