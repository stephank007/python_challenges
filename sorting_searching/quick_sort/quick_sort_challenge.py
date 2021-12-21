#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement quick sort.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is a naive solution sufficient (ie not in-place)?
#     * Yes
# * Are duplicates allowed?
#     * Yes
# * Can we assume the input is valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * Empty input -> []
# * One element -> [element]
# * Two or more elements

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/quick_sort/quick_sort_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class QuickSort(object):

    def sort(self, data):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_quick_sort.py
import unittest


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        quick_sort = QuickSort()

        print('None input')
        self.assertRaises(TypeError, quick_sort.sort, None)

        print('Empty input')
        self.assertEqual(quick_sort.sort([]), [])

        print('One element')
        self.assertEqual(quick_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(quick_sort.sort(data), sorted(data))

        print('Success: test_quick_sort\n')


def main():
    test = TestQuickSort()
    test.test_quick_sort()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/quick_sort/quick_sort_solution.ipynb) for a discussion on algorithms and code solutions.
