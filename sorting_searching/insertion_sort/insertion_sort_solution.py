#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement insertion sort.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is a naive solution sufficient?
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
# Wikipedia's animation:
# ![alt text](http://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)
# 
# * For each value index 1 to n - 1
#     * Compare with all elements to the left of the current value to determine new insertion point
#         * Hold current value in temp variable
#         * Shift elements from new insertion point right
#         * Insert value in temp variable
#         * Break
# 
# Complexity:
# * Time: O(n^2) average, worst.  O(1) best if input is already sorted
# * Space: O(1) for the iterative solution
# 
# Misc: 
# 
# * In-place
# * Stable
# 
# Insertion sort works well for very small datasets where most of the input is already sorted.

# ## Code

# In[1]:


class InsertionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[l+1:r+1] = data[l:r]
                    data[l] = temp
        return data


# ## Unit Test
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_insertion_sort.py', "import unittest\n\n\nclass TestInsertionSort(unittest.TestCase):\n\n    def test_insertion_sort(self):\n        insertion_sort = InsertionSort()\n\n        print('None input')\n        self.assertRaises(TypeError, insertion_sort.sort, None)\n\n        print('Empty input')\n        self.assertEqual(insertion_sort.sort([]), [])\n\n        print('One element')\n        self.assertEqual(insertion_sort.sort([5]), [5])\n\n        print('Two or more elements')\n        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]\n        self.assertEqual(insertion_sort.sort(data), sorted(data))\n\n        print('Success: test_insertion_sort')\n\n\ndef main():\n    test = TestInsertionSort()\n    test.test_insertion_sort()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_insertion_sort.py')

