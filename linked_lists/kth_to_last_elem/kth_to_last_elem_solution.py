#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the kth to last element of a linked list.
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
# * Can we assume k is a valid integer?
#     * Yes
# * If k = 0, does this return the last element?
#     * Yes
# * What happens if k is greater than or equal to the length of the linked list?
#     * Return None
# * Can you use additional data structures?
#     * No
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes

# ## Test Cases
# 
# * Empty list -> None
# * k is >= the length of the linked list -> None
# * One element, k = 0 -> element
# * General case with many elements, k < length of linked list

# ## Algorithm
# 
# * Setup two pointers, fast and slow
# * Give fast a headstart, incrementing it once if k = 1, twice if k = 2, ...
# * Increment both pointers until fast reaches the end
# * Return the value of slow
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')


# In[2]:


class MyLinkedList(LinkedList):

    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head

        # Give fast a headstart, incrementing it
        # once for k = 1, twice for k = 2, etc
        for _ in range(k):
            fast = fast.next
            # If k >= num elements, return None
            if fast is None:
                return None

        # Increment both pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_kth_to_last_elem.py', "import unittest\n\n\nclass Test(unittest.TestCase):\n\n    def test_kth_to_last_elem(self):\n        print('Test: Empty list')\n        linked_list = MyLinkedList(None)\n        self.assertEqual(linked_list.kth_to_last_elem(0), None)\n\n        print('Test: k >= len(list)')\n        self.assertEqual(linked_list.kth_to_last_elem(100), None)\n\n        print('Test: One element, k = 0')\n        head = Node(2)\n        linked_list = MyLinkedList(head)\n        self.assertEqual(linked_list.kth_to_last_elem(0), 2)\n\n        print('Test: General case')\n        linked_list.insert_to_front(1)\n        linked_list.insert_to_front(3)\n        linked_list.insert_to_front(5)\n        linked_list.insert_to_front(7)\n        self.assertEqual(linked_list.kth_to_last_elem(2), 3)\n\n        print('Success: test_kth_to_last_elem')\n\n\ndef main():\n    test = Test()\n    test.test_kth_to_last_elem()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_kth_to_last_elem.py')

