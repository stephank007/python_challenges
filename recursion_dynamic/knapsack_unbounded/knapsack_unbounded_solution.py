#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine the max total value you can carry.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# We'll use bottom up dynamic programming to build a table.  
# 
# Taking what we learned with the 0/1 knapsack problem, we could solve the problem like the following:
# 
# <pre>
# 
# v = value
# w = weight
# 
#                j              
#     -------------------------------------------------
#     | v | w || 0 | 1 | 2 | 3 | 4 | 5 |  6 |  7 |  8  |
#     -------------------------------------------------
#     | 0 | 0 || 0 | 0 | 0 | 0 | 0 | 0 |  0 |  0 |  0  |
#   a | 1 | 1 || 0 | 1 | 2 | 3 | 4 | 5 |  6 |  7 |  8  |
# i b | 3 | 2 || 0 | 1 | 3 | 4 | 6 | 7 |  9 | 10 | 12  |
#   c | 7 | 4 || 0 | 1 | 3 | 4 | 7 | 8 | 10 | 11 | 14  |
#     -------------------------------------------------
# 
# i = row
# j = col
# 
# </pre>
# 
# However, unlike the 0/1 knapsack variant, we don't actually need to keep space of O(n * w), where n is the number of items and w is the total weight.  We just need a single array that we update after we process each item:
# 
# <pre>
# 
#     -------------------------------------------------
#     | v | w || 0 | 1 | 2 | 3 | 4 | 5 |  6 |  7 |  8  |
#     -------------------------------------------------
# 
#     -------------------------------------------------
#   a | 1 | 1 || 0 | 1 | 2 | 3 | 4 | 5 |  6 |  7 |  8  |
#     -------------------------------------------------
# 
#     -------------------------------------------------
#   b | 3 | 2 || 0 | 1 | 3 | 4 | 6 | 7 |  9 | 10 | 12  |
#     -------------------------------------------------
# 
#     -------------------------------------------------
#   c | 7 | 4 || 0 | 1 | 3 | 4 | 7 | 8 | 10 | 11 | 14  |
#     -------------------------------------------------
# 
# if j >= items[i].weight:
#     T[j] = max(items[i].value + T[j - items[i].weight],
#                T[j])
# 
# </pre>
# 
# Complexity:
# * Time: O(n * w), where n is the number of items and w is the total weight
# * Space: O(w), where w is the total weight

# ## Code

# ### Item Class

# In[1]:


class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


# ### Knapsack Bottom Up

# In[2]:


class Knapsack(object):

    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError('items or total_weight cannot be None')
        if not items or total_weight == 0:
            return 0
        num_rows = len(items)
        num_cols = total_weight + 1
        T = [0] * (num_cols)
        for i in range(num_rows):
            for j in range(num_cols):
                if j >= items[i].weight:
                    T[j] = max(items[i].value + T[j - items[i].weight],
                               T[j])
        return T[-1]


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_knapsack_unbounded.py', "import unittest\n\n\nclass TestKnapsack(unittest.TestCase):\n\n    def test_knapsack(self):\n        knapsack = Knapsack()\n        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)\n        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)\n        items = []\n        items.append(Item(label='a', value=1, weight=1))\n        items.append(Item(label='b', value=3, weight=2))\n        items.append(Item(label='c', value=7, weight=4))\n        total_weight = 8\n        expected_value = 14\n        results = knapsack.fill_knapsack(items, total_weight)\n        total_weight = 7\n        expected_value = 11\n        results = knapsack.fill_knapsack(items, total_weight)\n        self.assertEqual(results, expected_value)\n        print('Success: test_knapsack')\n\ndef main():\n    test = TestKnapsack()\n    test.test_knapsack()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_knapsack_unbounded.py')

