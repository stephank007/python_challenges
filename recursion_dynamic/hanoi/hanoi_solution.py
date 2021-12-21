#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement the [Towers of Hanoi](http://en.wikipedia.org/wiki/Tower_of_Hanoi) with 3 towers and N disks.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume we already have a stack class that can be used for this problem?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None tower(s) -> Exception
# * 0 disks -> None
# * 1 disk
# * 2 or more disks

# ## Algorithm
# 
# * Create three stacks to represent each tower
# * def hanoi(n, src, dest, buffer):
#     * If 0 disks return
#     * hanoi(n-1, src, buffer, dest)
#     * Move remaining element from src to dest
#     * hanoi(n-1, buffer, dest, src)
# 
# Complexity:
# * Time: O(2^n)
# * Space: O(m) where m is the number of recursion levels

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../../stacks_queues/stack/stack.py')


# In[2]:


class Hanoi(object):

    def move_disks(self, num_disks, src, dest, buff):
        if src is None or dest is None or buff is None:
            raise TypeError('Cannot have a None input')
        self._move_disks(num_disks, src, dest, buff)

    def _move_disks(self, num_disks, src, dest, buff):
        if num_disks == 0:
            return
        self.move_disks(num_disks - 1, src, buff, dest)
        dest.push(src.pop())
        self.move_disks(num_disks - 1, buff, dest, src)


# ## Unit Test
# 
# 

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_hanoi.py', "import unittest\n\n\nclass TestHanoi(unittest.TestCase):\n\n    def test_hanoi(self):\n        hanoi = Hanoi()\n        num_disks = 3\n        src = Stack()\n        buff = Stack()\n        dest = Stack()\n\n        print('Test: None towers')\n        self.assertRaises(TypeError, hanoi.move_disks, num_disks, None, None, None)\n\n        print('Test: 0 disks')\n        hanoi.move_disks(num_disks, src, dest, buff)\n        self.assertEqual(dest.pop(), None)\n\n        print('Test: 1 disk')\n        src.push(5)\n        hanoi.move_disks(num_disks, src, dest, buff)\n        self.assertEqual(dest.pop(), 5)\n\n        print('Test: 2 or more disks')\n        for disk_index in range(num_disks, -1, -1):\n            src.push(disk_index)\n        hanoi.move_disks(num_disks, src, dest, buff)\n        for disk_index in range(0, num_disks):\n            self.assertEqual(dest.pop(), disk_index)\n\n        print('Success: test_hanoi')\n\n\ndef main():\n    test = TestHanoi()\n    test.test_hanoi()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_hanoi.py')

