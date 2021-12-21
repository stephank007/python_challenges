#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given an array of (unix_timestamp, num_people, EventType.ENTER or EventType.EXIT), find the busiest period.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the input array is valid?
#     * Check for None
# * Can we assume the elements of the input array are valid?
#     * Yes
# * Is the input sorted by time?
#     * No
# * Can you have enter and exit elements for the same timestamp?
#     * Yes you can, order of enter and exit is not guaranteed
# * Could we have multiple enter events (or multiple exit events) for the same timestamp?
#     * No
# * What is the format of the output?
#     * An array of timestamps [t1, t2]
# * Can we assume the starting number of people is zero?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * [] -> None
# * General case
# 
# <pre>
# timestamp  num_people  event_type
# 1          2           EventType.ENTER
# 3          1           EventType.ENTER
# 3          2           EventType.EXIT
# 7          3           EventType.ENTER
# 8          2           EventType.EXIT
# 9          2           EventType.EXIT
# 
# result = Period(7, 8)
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


from enum import Enum


class Data(object):

    def __init__(self, timestamp, num_people, event_type):
        self.timestamp = timestamp
        self.num_people = num_people
        self.event_type = event_type

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class Period(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return str(self.start) + ', ' + str(self.end)


class EventType(Enum):

    ENTER = 0
    EXIT = 1


# In[ ]:


class Solution(object):

    def find_busiest_period(self, data):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_find_busiest_period.py
import unittest


class TestSolution(unittest.TestCase):

    def test_find_busiest_period(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_busiest_period, None)
        self.assertEqual(solution.find_busiest_period([]), None)
        data = [
            Data(3, 2, EventType.EXIT),
            Data(1, 2, EventType.ENTER),
            Data(3, 1, EventType.ENTER),
            Data(7, 3, EventType.ENTER),
            Data(9, 2, EventType.EXIT),
            Data(8, 2, EventType.EXIT),
        ]
        self.assertEqual(solution.find_busiest_period(data), Period(7, 8))
        print('Success: test_find_busiest_period')


def main():
    test = TestSolution()
    test.test_find_busiest_period()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
