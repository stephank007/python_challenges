#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given an array of (unix_timestamp, num_people, EventType.ENTER or EventType.EXIT), find the busiest period.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# 3          2           EventType.EXIT
# 1          2           EventType.ENTER
# 3          1           EventType.ENTER
# 7          3           EventType.ENTER
# 9          2           EventType.EXIT
# 8          2           EventType.EXIT
# 
# result = Period(7, 8)
# </pre>

# ## Algorithm
# 
# Since the input is not sorted, we'll need to sort it first by timestamp, ascending.
# 
# For each interval in the data set:
# 
# * If this is an "enter" event, increment `curr_people`, else, decrement
# * Since we can have an "enter" and "exit" event for the same timestamp, we'll need to look ahead one
#     * If the next element has the same timestamp, hold off (continue) on updating `max_people` and `max_period`
#     * Watch out for indexing out-of-bounds at the end of the array
# * Update `max_people` and `max_period`
# 
# Sorted:
# 
# <pre>
# timestamp  num_people  event_type       curr_people  max_people       max_period
# 1          2           EventType.ENTER  2            2                [1, 3]
# 3          1           EventType.ENTER  3            2 (not updated)  [1, 3]
# 3          2           EventType.EXIT   1            2                [3, 7]
# 7          3           EventType.ENTER  4            4                [7, 8]
# 8          2           EventType.EXIT   2            4                [7, 8]
# 9          2           EventType.EXIT   0            4                [7, 8]
# </pre>
# 
# Complexity:
# * Time: O(nlog(n)) for the sort
# * Space: O(1), assuming the sort is in-place

# ## Code

# In[1]:


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


# In[2]:


class Solution(object):

    def find_busiest_period(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if not data:
            return None
        data.sort()
        max_period = Period(0, 0)
        max_people = 0
        curr_people = 0
        for index, interval in enumerate(data):
            if interval.event_type == EventType.ENTER:
                curr_people += interval.num_people
            elif interval.event_type == EventType.EXIT:
                curr_people -= interval.num_people
            else:
                raise ValueError('Invalid event type')
            if (index < len(data) - 1 and 
                    data[index].timestamp == data[index + 1].timestamp):
                continue
            if curr_people > max_people:
                max_people = curr_people
                max_period.start = data[index].timestamp
                if index < len(data) - 1:
                    max_period.end = data[index + 1].timestamp
                else:
                    max_period.end = data[index].timestamp
        return max_period


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_find_busiest_period.py', "import unittest\n\n\nclass TestSolution(unittest.TestCase):\n\n    def test_find_busiest_period(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.find_busiest_period, None)\n        self.assertEqual(solution.find_busiest_period([]), None)\n        data = [\n            Data(3, 2, EventType.EXIT),\n            Data(1, 2, EventType.ENTER),\n            Data(3, 1, EventType.ENTER),\n            Data(7, 3, EventType.ENTER),\n            Data(9, 2, EventType.EXIT),\n            Data(8, 2, EventType.EXIT),\n        ]\n        self.assertEqual(solution.find_busiest_period(data), Period(7, 8))\n        print('Success: test_find_busiest_period')\n\n\ndef main():\n    test = TestSolution()\n    test.test_find_busiest_period()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_find_busiest_period.py')

