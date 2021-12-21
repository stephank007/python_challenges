#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement the [Towers of Hanoi](http://en.wikipedia.org/wiki/Tower_of_Hanoi) with 3 towers and N disks.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

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
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/hanoi/hanoi_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../../stacks_queues/stack/stack.py')
get_ipython().run_line_magic('load', '../../stacks_queues/stack/stack.py')


# In[ ]:


class Hanoi(object):

    def move_disks(self, num_disks, src, dest, buff):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_hanoi.py
import unittest


class TestHanoi(unittest.TestCase):

    def test_hanoi(self):
        hanoi = Hanoi()
        num_disks = 3
        src = Stack()
        buff = Stack()
        dest = Stack()

        print('Test: None towers')
        self.assertRaises(TypeError, hanoi.move_disks, num_disks, None, None, None)

        print('Test: 0 disks')
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), None)

        print('Test: 1 disk')
        src.push(5)
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), 5)

        print('Test: 2 or more disks')
        for disk_index in range(num_disks, -1, -1):
            src.push(disk_index)
        hanoi.move_disks(num_disks, src, dest, buff)
        for disk_index in range(0, num_disks):
            self.assertEqual(dest.pop(), disk_index)

        print('Success: test_hanoi')


def main():
    test = TestHanoi()
    test.test_hanoi()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/hanoi/hanoi_solution.ipynb) for a discussion on algorithms and code solutions.
