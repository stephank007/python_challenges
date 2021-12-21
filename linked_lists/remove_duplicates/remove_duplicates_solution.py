#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Remove duplicates from a linked list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm: Hash Map Lookup](#Algorithm:-Hash-Map-Lookup)
# * [Algorithm: In-Place](#Algorithm:-In-Place)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume this is a non-circular, singly linked list?
#     * Yes
# * Can you insert None values in the list?
#     * No
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes
# * Can we use additional data structures?
#     * Implement both solutions
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * Empty linked list -> []
# * One element linked list -> [element]
# * General case with no duplicates
# * General case with duplicates

# ## Algorithm: Hash Map Lookup
# 
# Loop through each node
# 
# * For each node
#     * If the node's value is in the hash map
#         * Delete the node
#     * Else
#         * Add node's value to the hash map
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Algorithm: In-Place
# 
# * For each node
#     * Compare node with every other node
#         * Delete nodes that match current node
# 
# Complexity:
# * Time: O(n^2)
# * Space: O(1)
# 
# Note:
# * We'll need to use a 'runner' to check every other node and compare it to the current node

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')


# In[2]:


class MyLinkedList(LinkedList):

    def remove_dupes(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set()
        while node is not None:
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

    def remove_dupes_single_pointer(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set({node.data})
        while node.next is not None:
            if node.next.data in seen_data:
                node.next = node.next.next
            else:
                seen_data.add(node.next.data)
                node = node.next

    def remove_dupes_in_place(self):
        curr = self.head
        while curr is not None:
            runner = curr
            while runner.next is not None:
                if runner.next.data == curr.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_remove_duplicates.py', "import unittest\n\n\nclass TestRemoveDupes(unittest.TestCase):\n\n    def test_remove_dupes(self, linked_list):\n        print('Test: Empty list')\n        linked_list.remove_dupes()\n        self.assertEqual(linked_list.get_all_data(), [])\n\n        print('Test: One element list')\n        linked_list.insert_to_front(2)\n        linked_list.remove_dupes()\n        self.assertEqual(linked_list.get_all_data(), [2])\n\n        print('Test: General case, duplicates')\n        linked_list.insert_to_front(1)\n        linked_list.insert_to_front(1)\n        linked_list.insert_to_front(3)\n        linked_list.insert_to_front(2)\n        linked_list.insert_to_front(3)\n        linked_list.insert_to_front(1)\n        linked_list.insert_to_front(1)\n        linked_list.remove_dupes()\n        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])\n\n        print('Test: General case, no duplicates')\n        linked_list.remove_dupes()\n        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])\n\n        print('Success: test_remove_dupes\\n')\n\n\ndef main():\n    test = TestRemoveDupes()\n    linked_list = MyLinkedList(None)\n    test.test_remove_dupes(linked_list)\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


run -i test_remove_duplicates.py

