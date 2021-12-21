#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the start of a linked list loop.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is this a singly linked list?
#     * Yes
# * Can we assume we are always passed a circular linked list?
#     * No
# * When we find a loop, do we return the node or the node's data?
#     * The node
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes

# ## Test Cases
# 
# * Empty list -> None
# * Not a circular linked list -> None
#     * One element
#     * Two or more elements
# * Circular linked list general case

# ## Algorithm
# 
# * Use two references `slow`, `fast`, initialized to the `head`
# * Increment `slow` and `fast` until they meet
#     * `fast` is incremented twice as fast as `slow`
#         * If `fast.next` is `None`, we do not have a circular list
# * When `slow` and `fast` meet, move `slow` to the `head`
# * Increment `slow` and `fast` one node at a time until they meet
# * Where they meet is the start of the loop
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')


# In[2]:


class MyLinkedList(LinkedList):

    def find_loop_start(self):
        if self.head is None or self.head.next is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        return slow


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_find_loop_start.py', "import unittest\n\n\nclass TestFindLoopStart(unittest.TestCase):\n\n    def test_find_loop_start(self):\n        print('Test: Empty list')\n        linked_list = MyLinkedList()\n        self.assertEqual(linked_list.find_loop_start(), None)\n\n        print('Test: Not a circular linked list: One element')\n        head = Node(1)\n        linked_list = MyLinkedList(head)\n        self.assertEqual(linked_list.find_loop_start(), None)\n\n        print('Test: Not a circular linked list: Two elements')\n        linked_list.append(2)\n        self.assertEqual(linked_list.find_loop_start(), None)\n\n        print('Test: Not a circular linked list: Three or more elements')\n        linked_list.append(3)\n        self.assertEqual(linked_list.find_loop_start(), None)\n\n        print('Test: General case: Circular linked list')\n        node10 = Node(10)\n        node9 = Node(9, node10)\n        node8 = Node(8, node9)\n        node7 = Node(7, node8)\n        node6 = Node(6, node7)\n        node5 = Node(5, node6)\n        node4 = Node(4, node5)\n        node3 = Node(3, node4)\n        node2 = Node(2, node3)\n        node1 = Node(1, node2)\n        node0 = Node(0, node1)\n        node10.next = node3\n        linked_list = MyLinkedList(node0)\n        self.assertEqual(linked_list.find_loop_start(), node3)\n\n        print('Success: test_find_loop_start')\n\n\ndef main():\n    test = TestFindLoopStart()\n    test.test_find_loop_start()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_find_loop_start.py')

