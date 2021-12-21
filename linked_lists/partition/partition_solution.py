#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume this is a non-circular, singly linked list?
#     * Yes
# * Do we expect the function to return a new list?
#     * Yes
# * Can we assume the input x is valid?
#     * Yes
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes
# * Can we create additional data structures?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * Empty list -> []
# * One element list -> [element]
# * Left linked list is empty
# * Right linked list is empty
# * General case
#     * Partition = 10
#     * Input: 4, 3, 13, 8, 10, 1, 10, 12
#     * Output: 4, 3, 8, 1, 10, 10, 13, 12

# ## Algorithm
# 
# * Create left and right linked lists
# * For each element in the list
#     * If elem < x, append to the left list
#     * else, append to the right list
# * Merge left and right lists
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')


# In[2]:


class MyLinkedList(LinkedList):

    def partition(self, data):
        if self.head is None:
            return
        left = MyLinkedList(None)
        right = MyLinkedList(None)
        curr = self.head

        # Build the left and right lists
        while curr is not None:
            if curr.data < data:
                left.append(curr.data)
            elif curr.data == data:
                right.insert_to_front(curr.data)
            else:
                right.append(curr.data)
            curr = curr.next
        curr_left = left.head
        if curr_left is None:
            return right
        else:
            # Merge the two lists
            while curr_left.next is not None:
                curr_left = curr_left.next
            curr_left.next = right.head
            return left


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_partition.py', "import unittest\n\n\nclass TestPartition(unittest.TestCase):\n\n    def test_partition(self):\n        print('Test: Empty list')\n        linked_list = MyLinkedList(None)\n        linked_list.partition(10)\n        self.assertEqual(linked_list.get_all_data(), [])\n\n        print('Test: One element list, left list empty')\n        linked_list = MyLinkedList(Node(5))\n        linked_list.partition(0)\n        self.assertEqual(linked_list.get_all_data(), [5])\n\n        print('Test: Right list is empty')\n        linked_list = MyLinkedList(Node(5))\n        linked_list.partition(10)\n        self.assertEqual(linked_list.get_all_data(), [5])\n\n        print('Test: General case')\n        # Partition = 10\n        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12\n        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12\n        linked_list = MyLinkedList(Node(12))\n        linked_list.insert_to_front(10)\n        linked_list.insert_to_front(14)\n        linked_list.insert_to_front(1)\n        linked_list.insert_to_front(10)\n        linked_list.insert_to_front(8)\n        linked_list.insert_to_front(13)\n        linked_list.insert_to_front(3)\n        linked_list.insert_to_front(4)\n        partitioned_list = linked_list.partition(10)\n        self.assertEqual(partitioned_list.get_all_data(),\n                     [4, 3, 8, 1, 10, 10, 13, 14, 12])\n\n        print('Success: test_partition')\n\n\ndef main():\n    test = TestPartition()\n    test.test_partition()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


run -i test_partition.py

