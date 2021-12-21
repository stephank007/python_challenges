#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a linked list with insert, append, find, delete, length, and print methods.
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
# * Do we keep track of the tail or just the head?
#     * Just the head
# * Can we insert None values?
#     * No

# ## Test Cases
# 
# ### Insert to Front
# 
# * Insert a None
# * Insert in an empty list
# * Insert in a list with one element or more elements
# 
# ### Append
# 
# * Append a None
# * Append in an empty list
# * Insert in a list with one element or more elements
# 
# ### Find
# 
# * Find a None
# * Find in an empty list
# * Find in a list with one element or more matching elements
# * Find in a list with no matches
# 
# ### Delete
# 
# * Delete a None
# * Delete in an empty list
# * Delete in a list with one element or more matching elements
# * Delete in a list with no matches
# 
# ### Length
# 
# * Length of zero or more elements
# 
# ### Print
# 
# * Print an empty list
# * Print a list with one or more elements

# ## Algorithm
# 
# ### Insert to Front
# 
# * If the data we are inserting is None, return
# * Create a node with the input data, set node.next to head
# * Assign the head to the node
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Append
# 
# * If the data we are inserting is None, return
# * Create a node with the input data
# * If this is an empty list
#     * Assign the head to the node
# * Else
#     * Iterate to the end of the list
#     * Set the final node's next to the new node
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)
# 
# ### Find
# 
# * If data we are finding is None, return
# * If the list is empty, return
# * For each node
#     * If the value is a match, return it
#     * Else, move on to the next node
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)
# 
# ### Delete
# 
# * If data we are deleting is None, return
# * If the list is empty, return
# * For each node, keep track of previous and current node
#     * If the value we are deleting is a match in the current node
#         * Update previous node's next pointer to the current node's next pointer
#         * We do not have have to explicitly delete in Python
#     * Else, move on to the next node
# * As an alternative, we could avoid the use of two pointers by evaluating the current node's next value:
#     * If the next value is a match, set the current node's next to next.next
#     * Special care should be taken if deleting the head node
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)
# 
# ### Length
# 
# * For each node
#     * Increase length counter
#     
# Complexity:
# * Time: O(n)
# * Space: O(1)
# 
# ### Print
# 
# * For each node
#     * Print the node's value
#     
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'linked_list.py', 'class Node(object):\n\n    def __init__(self, data, next=None):\n        self.next = next\n        self.data = data\n\n    def __str__(self):\n        return self.data\n\n\nclass LinkedList(object):\n\n    def __init__(self, head=None):\n        self.head = head\n\n    def __len__(self):\n        curr = self.head\n        counter = 0\n        while curr is not None:\n            counter += 1\n            curr = curr.next\n        return counter\n\n    def insert_to_front(self, data):\n        if data is None:\n            return None\n        node = Node(data, self.head)\n        self.head = node\n        return node\n\n    def append(self, data):\n        if data is None:\n            return None\n        node = Node(data)\n        if self.head is None:\n            self.head = node\n            return node\n        curr_node = self.head\n        while curr_node.next is not None:\n            curr_node = curr_node.next\n        curr_node.next = node\n        return node\n\n    def find(self, data):\n        if data is None:\n            return None\n        curr_node = self.head\n        while curr_node is not None:\n            if curr_node.data == data:\n                return curr_node\n            curr_node = curr_node.next\n        return None\n\n    def delete(self, data):\n        if data is None:\n            return\n        if self.head is None:\n            return\n        if self.head.data == data:\n            self.head = self.head.next\n            return\n        prev_node = self.head\n        curr_node = self.head.next\n        while curr_node is not None:\n            if curr_node.data == data:\n                prev_node.next = curr_node.next\n                return\n            prev_node = curr_node\n            curr_node = curr_node.next\n\n    def delete_alt(self, data):\n        if data is None:\n            return\n        if self.head is None:\n            return\n        curr_node = self.head\n        if curr_node.data == data:\n            curr_node = curr_node.next\n            return\n        while curr_node.next is not None:\n            if curr_node.next.data == data:\n                curr_node.next = curr_node.next.next\n                return\n            curr_node = curr_node.next\n\n    def print_list(self):\n        curr_node = self.head\n        while curr_node is not None:\n            print(curr_node.data)\n            curr_node = curr_node.next\n\n    def get_all_data(self):\n        data = []\n        curr_node = self.head\n        while curr_node is not None:\n            data.append(curr_node.data)\n            curr_node = curr_node.next\n        return data')


# In[2]:


get_ipython().run_line_magic('run', 'linked_list.py')


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_linked_list.py', "import unittest\n\n\nclass TestLinkedList(unittest.TestCase):\n\n    def test_insert_to_front(self):\n        print('Test: insert_to_front on an empty list')\n        linked_list = LinkedList(None)\n        linked_list.insert_to_front(10)\n        self.assertEqual(linked_list.get_all_data(), [10])\n\n        print('Test: insert_to_front on a None')\n        linked_list.insert_to_front(None)\n        self.assertEqual(linked_list.get_all_data(), [10])\n\n        print('Test: insert_to_front general case')\n        linked_list.insert_to_front('a')\n        linked_list.insert_to_front('bc')\n        self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])\n\n        print('Success: test_insert_to_front\\n')\n\n    def test_append(self):\n        print('Test: append on an empty list')\n        linked_list = LinkedList(None)\n        linked_list.append(10)\n        self.assertEqual(linked_list.get_all_data(), [10])\n\n        print('Test: append a None')\n        linked_list.append(None)\n        self.assertEqual(linked_list.get_all_data(), [10])\n\n        print('Test: append general case')\n        linked_list.append('a')\n        linked_list.append('bc')\n        self.assertEqual(linked_list.get_all_data(), [10, 'a', 'bc'])\n\n        print('Success: test_append\\n')\n\n    def test_find(self):\n        print('Test: find on an empty list')\n        linked_list = LinkedList(None)\n        node = linked_list.find('a')\n        self.assertEqual(node, None)\n\n        print('Test: find a None')\n        head = Node(10)\n        linked_list = LinkedList(head)\n        node = linked_list.find(None)\n        self.assertEqual(node, None)\n\n        print('Test: find general case with matches')\n        head = Node(10)\n        linked_list = LinkedList(head)\n        linked_list.insert_to_front('a')\n        linked_list.insert_to_front('bc')\n        node = linked_list.find('a')\n        self.assertEqual(str(node), 'a')\n\n        print('Test: find general case with no matches')\n        node = linked_list.find('aaa')\n        self.assertEqual(node, None)\n\n        print('Success: test_find\\n')\n\n    def test_delete(self):\n        print('Test: delete on an empty list')\n        linked_list = LinkedList(None)\n        linked_list.delete('a')\n        self.assertEqual(linked_list.get_all_data(), [])\n\n        print('Test: delete a None')\n        head = Node(10)\n        linked_list = LinkedList(head)\n        linked_list.delete(None)\n        self.assertEqual(linked_list.get_all_data(), [10])\n\n        print('Test: delete general case with matches')\n        head = Node(10)\n        linked_list = LinkedList(head)\n        linked_list.insert_to_front('a')\n        linked_list.insert_to_front('bc')\n        linked_list.delete('a')\n        self.assertEqual(linked_list.get_all_data(), ['bc', 10])\n\n        print('Test: delete general case with no matches')\n        linked_list.delete('aa')\n        self.assertEqual(linked_list.get_all_data(), ['bc', 10])\n\n        print('Success: test_delete\\n')\n\n    def test_len(self):\n        print('Test: len on an empty list')\n        linked_list = LinkedList(None)\n        self.assertEqual(len(linked_list), 0)\n\n        print('Test: len general case')\n        head = Node(10)\n        linked_list = LinkedList(head)\n        linked_list.insert_to_front('a')\n        linked_list.insert_to_front('bc')\n        self.assertEqual(len(linked_list), 3)\n\n        print('Success: test_len\\n')\n\n\ndef main():\n    test = TestLinkedList()\n    test.test_insert_to_front()\n    test.test_append()\n    test.test_find()\n    test.test_delete()\n    test.test_len()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_linked_list.py')

