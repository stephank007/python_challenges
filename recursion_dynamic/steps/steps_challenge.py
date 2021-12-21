#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: You are running up n steps.  If you can take a single, double, or triple step, how many possible ways are there to run up to the nth step?
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * If n == 0, what should the result be?
#     * Go with 1, but discuss different approaches
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None or negative input -> Exception
# * n == 0 -> 1
# * n == 1 -> 1
# * n == 2 -> 2
# * n == 3 -> 4
# * n == 4 -> 7
# * n == 10 -> 274

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Steps(object):

    def count_ways(self, num_steps):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_steps.py
import unittest


class TestSteps(unittest.TestCase):

    def test_steps(self):
        steps = Steps()
        self.assertRaises(TypeError, steps.count_ways, None)
        self.assertRaises(TypeError, steps.count_ways, -1)
        self.assertEqual(steps.count_ways(0), 1)
        self.assertEqual(steps.count_ways(1), 1)
        self.assertEqual(steps.count_ways(2), 2)
        self.assertEqual(steps.count_ways(3), 4)
        self.assertEqual(steps.count_ways(4), 7)
        self.assertEqual(steps.count_ways(10), 274)
        print('Success: test_steps')


def main():
    test = TestSteps()
    test.test_steps()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
