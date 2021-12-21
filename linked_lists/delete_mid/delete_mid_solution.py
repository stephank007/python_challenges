#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Delete a node in the middle, given only access to that node.
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
# * What if the final node is being deleted, do we make it a dummy with value None?
#     * Yes
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes

# ## Test Cases
# 
# * Delete on empty list -> None
# * Delete None -> None
# * Delete on one node -> [None]
# * Delete on multiple nodes

# ## Algorithm
# 
# We'll need two pointers, one to the current node and one to the next node.  We will copy the next node's data to the current node's data (effectively deleting the current node) and update the current node's next pointer.
# 
# * set curr.data to next.data
# * set curr.next to next.next
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')


# In[2]:


class MyLinkedList(LinkedList):

    def delete_node(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_delete_mid.py', "import unittest\n\n\nclass TestDeleteNode(unittest.TestCase):\n\n    def test_delete_node(self):\n        print('Test: Empty list, null node to delete')\n        linked_list = MyLinkedList(None)\n        linked_list.delete_node(None)\n        self.assertEqual(linked_list.get_all_data(), [])\n\n        print('Test: One node')\n        head = Node(2)\n        linked_list = MyLinkedList(head)\n        linked_list.delete_node(head)\n        self.assertEqual(linked_list.get_all_data(), [None])\n\n        print('Test: Multiple nodes')\n        linked_list = MyLinkedList(None)\n        node0 = linked_list.insert_to_front(2)\n        node1 = linked_list.insert_to_front(3)\n        node2 = linked_list.insert_to_front(4)\n        node3 = linked_list.insert_to_front(1)\n        linked_list.delete_node(node1)\n        self.assertEqual(linked_list.get_all_data(), [1, 4, 2])\n\n        print('Test: Multiple nodes, delete last element')\n        linked_list = MyLinkedList(None)\n        node0 = linked_list.insert_to_front(2)\n        node1 = linked_list.insert_to_front(3)\n        node2 = linked_list.insert_to_front(4)\n        node3 = linked_list.insert_to_front(1)\n        linked_list.delete_node(node0)\n        self.assertEqual(linked_list.get_all_data(), [1, 4, 3, None])\n\n        print('Success: test_delete_node')\n\n\ndef main():\n    test = TestDeleteNode()\n    test.test_delete_node()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_delete_mid.py')

