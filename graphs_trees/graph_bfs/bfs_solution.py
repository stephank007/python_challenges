#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement breadth-first search on a graph.
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
# * Order of nodes visited: [0, 1, 4, 5, 3, 2]

# ## Algorithm
# 
# We generally use breadth-first search to determine the shortest path.
# 
# * Add the current node to the queue and mark it as visited
# * While the queue is not empty
#     * Dequeue a node and visit it
#     * Iterate through each adjacent node
#         * If the node has not been visited, add it to the queue and mark it as visited
# 
# Complexity:
# * Time: O(V + E), where V = number of vertices and E = number of edges
# * Space: O(V)
# 
# Note on space complexity from [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search):
# * When the number of vertices in the graph is known ahead of time, and additional data structures are used to determine which vertices have already been added to the queue, the space complexity can be expressed as O(V) 
# * If the graph is represented by an adjacency list it occupies O(V + E) space in memory
# * If the graph is represented by an adjacency matrix representation, it occupies O(V^2)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../graph/graph.py')


# In[2]:


from collections import deque


class GraphBfs(Graph):

    def bfs(self, root, visit_func):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        root.visit_state = State.visited
        while queue:
            node = queue.popleft()
            visit_func(node)
            for adjacent_node in node.adj_nodes.values():
                if adjacent_node.visit_state == State.unvisited:
                    queue.append(adjacent_node)
                    adjacent_node.visit_state = State.visited


# ## Unit Test

# In[3]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[4]:


get_ipython().run_cell_magic('writefile', 'test_bfs.py', 'import unittest\n\n\nclass TestBfs(unittest.TestCase):\n\n    def __init__(self, *args, **kwargs):\n        super(TestBfs, self).__init__()\n        self.results = Results()\n\n    def test_bfs(self):\n        nodes = []\n        graph = GraphBfs()\n        for id in range(0, 6):\n            nodes.append(graph.add_node(id))\n        graph.add_edge(0, 1, 5)\n        graph.add_edge(0, 4, 3)\n        graph.add_edge(0, 5, 2)\n        graph.add_edge(1, 3, 5)\n        graph.add_edge(1, 4, 4)\n        graph.add_edge(2, 1, 6)\n        graph.add_edge(3, 2, 7)\n        graph.add_edge(3, 4, 8)\n        graph.bfs(nodes[0], self.results.add_result)\n        self.assertEqual(str(self.results), "[0, 1, 4, 5, 3, 2]")\n\n        print(\'Success: test_bfs\')\n\n\ndef main():\n    test = TestBfs()\n    test.test_bfs()\n\n\nif __name__ == \'__main__\':\n    main()')


# In[5]:


get_ipython().run_line_magic('run', '-i test_bfs.py')

