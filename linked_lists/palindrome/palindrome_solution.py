#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine if a linked list is a palindrome.
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
# * Is a single character or number a palindrome?
#     * No
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes
# * Can we use additional data structures?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# 
# * Empty list -> False
# * Single element list -> False
# * Two or more element list, not a palindrome -> False
# * General case: Palindrome with even length -> True
# * General case: Palindrome with odd length -> True

# ## Algorithm
# 
# * Reverse the linked list
#     * Iterate through the current linked list
#         * Insert to front the current node into a new linked list
# * Compare the reversed list with the original list
#     * Only need to compare the first half
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# Note:
# * We could also do this iteratively, using a stack to effectively reverse the first half of the string.

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')


# In[2]:


from __future__ import division


class MyLinkedList(LinkedList):

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        curr = self.head
        reversed_list = MyLinkedList()
        length = 0

        # Reverse the linked list
        while curr is not None:
            reversed_list.insert_to_front(curr.data)
            length += 1
            curr = curr.next

        # Compare the reversed list with the original list
        # Only need to compare the first half
        iterations = length // 2
        curr = self.head
        curr_reversed = reversed_list.head
        for _ in range(iterations):
            if curr.data != curr_reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
        return True


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_palindrome.py', "import unittest\n\n\nclass TestPalindrome(unittest.TestCase):\n\n    def test_palindrome(self):\n        print('Test: Empty list')\n        linked_list = MyLinkedList()\n        self.assertEqual(linked_list.is_palindrome(), False)\n\n        print('Test: Single element list')\n        head = Node(1)\n        linked_list = MyLinkedList(head)\n        self.assertEqual(linked_list.is_palindrome(), False)\n\n        print('Test: Two element list, not a palindrome')\n        linked_list.append(2)\n        self.assertEqual(linked_list.is_palindrome(), False)\n\n        print('Test: General case: Palindrome with even length')\n        head = Node('a')\n        linked_list = MyLinkedList(head)\n        linked_list.append('b')\n        linked_list.append('b')\n        linked_list.append('a')\n        self.assertEqual(linked_list.is_palindrome(), True)\n\n        print('Test: General case: Palindrome with odd length')\n        head = Node(1)\n        linked_list = MyLinkedList(head)\n        linked_list.append(2)\n        linked_list.append(3)\n        linked_list.append(2)\n        linked_list.append(1)\n        self.assertEqual(linked_list.is_palindrome(), True)\n\n        print('Success: test_palindrome')\n\n\ndef main():\n    test = TestPalindrome()\n    test.test_palindrome()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_palindrome.py')

