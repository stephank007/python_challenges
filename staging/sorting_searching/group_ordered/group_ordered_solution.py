#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [wdonahoe](https://github.com/wdonahoe). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a function that groups identical items based on their order in the list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm: Modified Selection Sort](#Algorithm: Modified Selection Sort)
# * [Code: Modified Selection Sort](#Code: Modified Selection Sort)
# * [Algorithm: Ordered Dict](#Algorithm: Ordered Dict)
# * [Code: Ordered Dict](#Code:-Ordered-Dict)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we use extra data structures?
#     * Yes

# ## Test Cases
# 
# * group_ordered([1,2,1,3,2]) -> [1,1,2,2,3]
# * group_ordered(['a','b','a') -> ['a','a','b']
# * group_ordered([1,1,2,3,4,5,2,1]-> [1,1,1,2,2,3,4,5]
# * group_ordered([]) -> []
# * group_ordered([1]) -> [1]
# * group_ordered(None) -> None
# 

# ## Algorithm: Modified Selection Sort
# 
# * Save the relative position of the first-occurrence of each item in a list.
# * Iterate through list of unique items.
#     * Keep an outer index; scan rest of list, swapping matching items with outer index and incrementing outer index each time. 
#     
# Complexity:
# * Time: O(n^2)
# * Space: O(n)

# # Code: Modified Selection Sort

# In[1]:


def make_order_list(list_in):
    order_list = []
    for item in list_in:
        if item not in order_list:
            order_list.append(item)
    return order_list


def group_ordered(list_in):
    if list_in is None:
        return None
    order_list = make_order_list(list_in)
    current = 0
    for item in order_list:
        search = current + 1
        while True:
            try:
                if list_in[search] != item:
                    search += 1
                else:
                    current += 1
                    list_in[current], list_in[search] = list_in[search], list_in[current]
                    search += 1
            except IndexError:
                break
    return list_in


# ## Algorithm: Ordered Dict.
# 
# * Use an ordered dict to track insertion order of each key
# * Flatten list of values.
# 
# Complexity:
# 
# * Time: O(n)
# * Space: O(n)

# ## Code: Ordered Dict

# In[2]:


from collections import OrderedDict

def group_ordered_alt(list_in):
    if list_in is None:
        return None
    result = OrderedDict()
    for value in list_in:
        result.setdefault(value, []).append(value)
    return [v for group in result.values() for v in group]


# ## Unit Test
# 
# #### The following unit test is expected to fail until you solve the challenge.

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_group_ordered.py', 'import unittest\n\n\nclass TestGroupOrdered(unittest.TestCase):\n    def test_group_ordered(self, func):\n\n        self.assertEqual(func(None), None)\n        print(\'Success: \' + func.__name__ + " None case.")\n        self.assertEqual(func([]), [])\n        print(\'Success: \' + func.__name__ + " Empty case.")\n        self.assertEqual(func([1]), [1])\n        print(\'Success: \' + func.__name__ + " Single element case.")\n        self.assertEqual(func([1, 2, 1, 3, 2]), [1, 1, 2, 2, 3])\n        self.assertEqual(func([\'a\', \'b\', \'a\']), [\'a\', \'a\', \'b\'])\n        self.assertEqual(func([1, 1, 2, 3, 4, 5, 2, 1]), [1, 1, 1, 2, 2, 3, 4, 5])\n        self.assertEqual(func([1, 2, 3, 4, 3, 4]), [1, 2, 3, 3, 4, 4])\n        print(\'Success: \' + func.__name__)\n\n\ndef main():\n    test = TestGroupOrdered()\n    test.test_group_ordered(group_ordered)\n    try:\n        test.test_group_ordered(group_ordered_alt)\n    except NameError:\n        # Alternate solutions are only defined\n        # in the solutions file\n        pass\n\nif __name__ == \'__main__\':\n    main()')


# In[4]:


get_ipython().run_line_magic('run', '-i test_group_ordered.py')

