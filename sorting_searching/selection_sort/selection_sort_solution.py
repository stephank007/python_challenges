#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement selection sort.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is a naive solution sufficient (ie not stable, not based on a heap)?
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
# * [] -> []
# * One element -> [element]
# * Two or more elements

# ## Algorithm
# 
# Wikipedia's animation:
# ![alt text](http://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)
# 
# We can do this recursively or iteratively.  Iteratively will be more efficient as it doesn't require the extra space overhead with the recursive calls.
# 
# * For each element
#     * Check every element to the right to find the min
#     * If min < current element, swap
# 
# Complexity:
# * Time: O(n^2) average, worst, best
# * Space: O(1) iterative, O(m) recursive where m is the recursion depth (unless tail-call elimination is available, then O(1))
#     * Note: Tail call elimination is not inherently available in Python, see the following [StackOverflow post](http://stackoverflow.com/a/13592002).
# 
# Misc: 
# 
# * In-place
# * Most implementations are not stable, due to swapping of values
# 
# Selection sort might be a good option if moving elements is more expensive than comparing them, as it requires at most n-1 swaps.
# 
# The finding of a minimum element can be done with a min heap, which would change the worst-case run time to O(n log(n)) and increase the space to O(n).  This is called a heap sort.

# ## Code

# In[1]:


class SelectionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if data[min_index] < data[i]:
                data[i], data[min_index] = data[min_index], data[i]
        return data

    def sort_iterative_alt(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            self._swap(data, i, self._find_min_index(data, i))
        return data

    def sort_recursive(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        return self._sort_recursive(data, start=0)

    def _sort_recursive(self, data, start):
        if data is None:
            return
        if start < len(data) - 1:
            swap(data, start, self._find_min_index(data, start))
            self._sort_recursive(data, start + 1)
        return data

    def _find_min_index(self, data, start):
        min_index = start
        for i in range(start + 1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        return min_index

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data


# ## Unit Test
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_selection_sort.py', "import unittest\n\n\nclass TestSelectionSort(unittest.TestCase):\n\n    def test_selection_sort(self, func):\n        print('None input')\n        self.assertRaises(TypeError, func, None)\n\n        print('Empty input')\n        self.assertEqual(func([]), [])\n\n        print('One element')\n        self.assertEqual(func([5]), [5])\n\n        print('Two or more elements')\n        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]\n        self.assertEqual(func(data), sorted(data))\n\n        print('Success: test_selection_sort\\n')\n\n\ndef main():\n    test = TestSelectionSort()\n    selection_sort = SelectionSort()\n    test.test_selection_sort(selection_sort.sort)\n    try:\n        test.test_selection_sort(selection_sort.sort_recursive)\n        test.test_selection_sort(selection_sort.sor_iterative_alt)\n    except NameError:\n        # Alternate solutions are only defined\n        # in the solutions file\n        pass\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_selection_sort.py')

