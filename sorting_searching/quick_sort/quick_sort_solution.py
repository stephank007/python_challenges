#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement quick sort.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Pythonic-Code](#Pythonic-Code)
# * [Unit Test](#Unit-Test)

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
# Wikipedia's animation:
# ![alt text](http://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)
# 
# * Set pivot to the middle element in the data
# * For each element:
#     * If current element is the pivot, continue
#     * If the element is less than the pivot, add to left array
#     * Else, add to right array
# * Recursively apply quicksort to the left array
# * Recursively apply quicksort to the right array
# * Merge the left array + pivot + right array
# 
# Complexity:
# * Time: O(n log(n)) average, best, O(n^2) worst
# * Space: O(n)
# 
# Misc:
# 
# * More sophisticated implementations are in-place, although they still take up recursion depth space
# * Most implementations are not stable
# 
# See [Quicksort on wikipedia](https://en.wikipedia.org/wiki/Quicksort):
# 
# Typically, quicksort is significantly faster in practice than other Θ(nlogn) algorithms, because its inner loop can be efficiently implemented on most architectures [presumably because it has good cache locality], and in most real-world data, it is possible to make design choices which minimize the probability of requiring quadratic time.
# 
# See: [Quicksort vs merge sort](http://stackoverflow.com/questions/70402/why-is-quicksort-better-than-mergesort)

# ## Code

# In[1]:


from __future__ import division


class QuickSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data
        equal = []
        left = []
        right = []
        pivot_index = len(data) // 2
        pivot_value = data[pivot_index]
        # Build the left and right partitions
        for item in data:
            if item == pivot_value:
                equal.append(item)
            elif item < pivot_value:
                left.append(item)
            else:
                right.append(item)
        # Recursively apply quick_sort
        left_ = self._sort(left)
        right_ = self._sort(right)
        return left_ + equal + right_


# ## Unit Test
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_quick_sort.py', "import unittest\n\n\nclass TestQuickSort(unittest.TestCase):\n\n    def test_quick_sort(self):\n        quick_sort = QuickSort()\n\n        print('None input')\n        self.assertRaises(TypeError, quick_sort.sort, None)\n\n        print('Empty input')\n        self.assertEqual(quick_sort.sort([]), [])\n\n        print('One element')\n        self.assertEqual(quick_sort.sort([5]), [5])\n\n        print('Two or more elements')\n        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]\n        self.assertEqual(quick_sort.sort(data), sorted(data))\n\n        print('Success: test_quick_sort\\n')\n\n\ndef main():\n    test = TestQuickSort()\n    test.test_quick_sort()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_quick_sort.py')

