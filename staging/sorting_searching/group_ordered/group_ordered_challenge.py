#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [wdonahoe](https://github.com/wdonahoe). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a function that groups identical items based on their order in the list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we use extra data structures?
#     * Yes

# ## Test Cases
# 
# * group_ordered([1,2,1,3,2])     ->     [1,1,2,2,3]
# * group_ordered(['a','b','a')    ->     ['a','a','b']
# * group_ordered([1,1,2,3,4,5,2,1]->     [1,1,1,2,2,3,4,5]
# * group_ordered([])              ->     []
# * group_ordered([1])             ->     [1]
# * group_ordered(None)            ->     None

# ## Algorithm
# 
# Refer to the [solution notebook](https://github.com/donnemartin/interactive-coding-challenges/templates/foo_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


def group_ordered(list_in):
    # TODO: Implement me
    pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_group_ordered.py
import unittest


class TestGroupOrdered(unittest.TestCase):
    def test_group_ordered(self, func):

        self.assertEqual(func(None), None)
        print('Success: ' + func.__name__ + " None case.")
        self.assertEqual(func([]), [])
        print('Success: ' + func.__name__ + " Empty case.")
        self.assertEqual(func([1]), [1])
        print('Success: ' + func.__name__ + " Single element case.")
        self.assertEqual(func([1, 2, 1, 3, 2]), [1, 1, 2, 2, 3])
        self.assertEqual(func(['a', 'b', 'a']), ['a', 'a', 'b'])
        self.assertEqual(func([1, 1, 2, 3, 4, 5, 2, 1]), [1, 1, 1, 2, 2, 3, 4, 5])
        self.assertEqual(func([1, 2, 3, 4, 3, 4]), [1, 2, 3, 3, 4, 4])
        print('Success: ' + func.__name__)


def main():
    test = TestGroupOrdered()
    test.test_group_ordered(group_ordered)
    try:
        test.test_group_ordered(group_ordered_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass

if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [solution notebook](https://github.com/donnemartin/interactive-coding-challenges/sorting_searching/group_ordered/group_ordered_solution.ipynb) for a discussion on algorithms and code solutions.
