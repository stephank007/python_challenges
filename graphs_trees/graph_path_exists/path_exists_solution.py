#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine whether there is a path between two nodes in a graph.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the graph directed?
#     * Yes
# * Can we assume we already have Graph and Node classes?
#     * Yes
# * Can we assume this is a connected graph?
#     * Yes
# * Can we assume the inputs are valid?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# Input:
# * `add_edge(source, destination, weight)`
# 
# ```
# graph.add_edge(0, 1, 5)
# graph.add_edge(0, 4, 3)
# graph.add_edge(0, 5, 2)
# graph.add_edge(1, 3, 5)
# graph.add_edge(1, 4, 4)
# graph.add_edge(2, 1, 6)
# graph.add_edge(3, 2, 7)
# graph.add_edge(3, 4, 8)
# ```
# 
# Result:
# * search_path(start=0, end=2) -> True
# * search_path(start=0, end=0) -> True
# * search_path(start=4, end=5) -> False

# ## Algorithm
# 
# To determine if there is a path, we can use either breadth-first or depth-first search.
# 
# Breadth-first search can also be used to determine the shortest path.  Depth-first search is easier to implement with just straight recursion, but often results in a longer path.
# 
# We'll use a breadth-first search approach:
# 
# * Add the start node to the queue and mark it as visited
# * If the start node is the end node, return True
# * While the queue is not empty
#     * Dequeue a node and visit it
#     * If the node is the end node, return True
#     * Iterate through each adjacent node
#         * If the node has not been visited, add it to the queue and mark it as visited
# * Return False
# 
# Complexity:
# * Time: O(V + E), where V = number of vertices and E = number of edges
# * Space: O(V + E)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../graph/graph.py')


# In[2]:


from collections import deque


class GraphPathExists(Graph):

    def path_exists(self, start, end):
        if start is None or end is None:
            return False
        if start is end:
            return True
        queue = deque()
        queue.append(start)
        start.visit_state = State.visited
        while queue:
            node = queue.popleft()
            if node is end:
                return True
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visit_state = State.visited
        return False


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_path_exists.py', "import unittest\n\n\nclass TestPathExists(unittest.TestCase):\n\n    def test_path_exists(self):\n        nodes = []\n        graph = GraphPathExists()\n        for id in range(0, 6):\n            nodes.append(graph.add_node(id))\n        graph.add_edge(0, 1, 5)\n        graph.add_edge(0, 4, 3)\n        graph.add_edge(0, 5, 2)\n        graph.add_edge(1, 3, 5)\n        graph.add_edge(1, 4, 4)\n        graph.add_edge(2, 1, 6)\n        graph.add_edge(3, 2, 7)\n        graph.add_edge(3, 4, 8)\n\n        self.assertEqual(graph.path_exists(nodes[0], nodes[2]), True)\n        self.assertEqual(graph.path_exists(nodes[0], nodes[0]), True)\n        self.assertEqual(graph.path_exists(nodes[4], nodes[5]), False)\n\n        print('Success: test_path_exists')\n\n\ndef main():\n    test = TestPathExists()\n    test.test_path_exists()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_path_exists.py')

