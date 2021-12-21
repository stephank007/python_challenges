#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Return all subsets of a set.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Should the resulting subsets be unique?
#     * Yes, treat 'ab' and 'bc' as the same
# * Is the empty set included as a subset?
#     * Yes
# * Are the inputs unique?
#     * No
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> None
# * [] -> [[]]
# * ['a'] -> [[], 
#             ['a']]
# * ['a', 'b'] -> [[], 
#                  ['a'], 
#                  ['b'], 
#                  ['a', 'b']]
# * ['a', 'b', 'c'] -> [[], 
#                       ['a'], 
#                       ['b'], 
#                       ['c'],
#                       ['a', 'b'], 
#                       ['a', 'c'], 
#                       ['b', 'c'],
#                       ['a', 'b', 'c']]
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Sets(object):

    def find_power_set_recursive(self, input_set):
        # TODO: Implement me
        pass

    def find_power_set_iterative(self, input_set):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_power_set.py
import unittest


class TestPowerSet(unittest.TestCase):

    def test_power_set(self):
        input_set = []
        expected = [[]]
        self.run_test(input_set, expected)
        input_set = ['a']
        expected = [['a'], []]
        self.run_test(input_set, expected)
        input_set = ['a', 'b']
        expected = [['a'], ['a', 'b'], ['b'], []]
        self.run_test(input_set, expected)
        input_set = ['a', 'b', 'c']
        expected = [['a'], ['a', 'b'], ['b'], ['a', 'c'], 
                    ['a', 'b', 'c'], ['b', 'c'], ['c'], []]
        self.run_test(input_set, expected)
        print('Success: test_power_set')

    def run_test(self, input_set, expected):
        combinatoric = Combinatoric()
        result = combinatoric.find_power_set_recursive(input_set)
        self.assertEqual(result, expected)
        result = combinatoric.find_power_set_iterative(input_set)
        self.assertEqual(result, expected)


def main():
    test = TestPowerSet()
    test.test_power_set()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
