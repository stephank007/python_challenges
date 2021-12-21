#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine the max total value you can carry.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we replace the items once they are placed in the knapsack?
#     * Yes, this is the unbounded knapsack problem
# * Can we split an item?
#     * No
# * Can we get an input item with weight of 0 or value of 0?
#     * No
# * Do we need to return the items that make up the max total value?
#     * No, just the total value
# * Can we assume the inputs are valid?
#     * No
# * Are the inputs in sorted order by val/weight?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * items or total weight is None -> Exception
# * items or total weight is 0 -> 0
# * General case
# 
# <pre>
# total_weight = 8
# items
#   v | w
#   0 | 0
# a 1 | 1
# b 3 | 2
# c 7 | 4
# 
# max value = 14 
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


# In[ ]:


class Knapsack(object):

    def fill_knapsack(self, input_items, total_weight):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_knapsack_unbounded.py
import unittest


class TestKnapsack(unittest.TestCase):

    def test_knapsack(self):
        knapsack = Knapsack()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=1, weight=1))
        items.append(Item(label='b', value=3, weight=2))
        items.append(Item(label='c', value=7, weight=4))
        total_weight = 8
        expected_value = 14
        results = knapsack.fill_knapsack(items, total_weight)
        total_weight = 7
        expected_value = 11
        results = knapsack.fill_knapsack(items, total_weight)
        self.assertEqual(results, expected_value)
        print('Success: test_knapsack')

def main():
    test = TestKnapsack()
    test.test_knapsack()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
