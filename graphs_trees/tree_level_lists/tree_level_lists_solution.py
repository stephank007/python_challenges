#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Create a list for each level of a binary tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is this a binary search tree?
#     * Yes
# * Should each level be a list of nodes?
#     * Yes
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * 5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11 -> [[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
# 
# Note: Each number in the result is actually a node containing the number

# ## Algorithm
# 
# We can use either a depth-first or a breadth-first search.  Intuitively, it seems like a breadth-first search might be a better fit as we are creating a linked list for each level.
# 
# We can use a modified breadth-first search that keeps track of parents as we build the linked list for the current level.
# 
# * Append the root to the current level's linked list `current`
# * While the `current` is not empty:
#     * Add `current` to `results`
#     * Set `parents` to `current` to prepare to go one level deeper
#     * Clear `current` so it can hold the next level
#     * For each `parent` in `parents`, add the children to `current`
# * Return the results
#     
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


class BstLevelLists(Bst):

    def create_level_lists(self):
        if self.root is None:
            return
        results = []
        current = []
        parents = []
        current.append(self.root)
        while current:
            results.append(current)
            parents = list(current)
            current = []
            for parent in parents:
                if parent.left is not None:
                    current.append(parent.left)
                if parent.right is not None:
                    current.append(parent.right)
        return results


# ## Unit Test

# In[3]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[4]:


get_ipython().run_cell_magic('writefile', 'test_tree_level_lists.py', "import unittest\n\n\nclass TestTreeLevelLists(unittest.TestCase):\n\n    def test_tree_level_lists(self):\n        bst = BstLevelLists(Node(5))\n        bst.insert(3)\n        bst.insert(8)\n        bst.insert(2)\n        bst.insert(4)\n        bst.insert(1)\n        bst.insert(7)\n        bst.insert(6)\n        bst.insert(9)\n        bst.insert(10)\n        bst.insert(11)\n\n        levels = bst.create_level_lists()\n        results_list = []\n        for level in levels:\n            results = Results()\n            for node in level:\n                results.add_result(node)\n            results_list.append(results)\n\n        self.assertEqual(str(results_list[0]), '[5]')\n        self.assertEqual(str(results_list[1]), '[3, 8]')\n        self.assertEqual(str(results_list[2]), '[2, 4, 7, 9]')\n        self.assertEqual(str(results_list[3]), '[1, 6, 10]')\n        self.assertEqual(str(results_list[4]), '[11]')\n\n        print('Success: test_tree_level_lists')\n\n\ndef main():\n    test = TestTreeLevelLists()\n    test.test_tree_level_lists()\n\n\nif __name__ == '__main__':\n    main()")


# In[5]:


get_ipython().run_line_magic('run', '-i test_tree_level_lists.py')

