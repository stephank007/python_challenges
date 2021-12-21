#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement depth-first search on a graph.
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
# * Order of nodes visited: [0, 1, 3, 2, 4, 5]

# ## Algorithm
# 
# If we want to visit every node in a graph, we generally prefer depth-first search since it is simpler (no need to use a queue).  For shortest path, we generally use breadth-first search.
# 
# * Visit the current node and mark it visited
# * Iterate through each adjacent node
#     * If the node has not been visited, call dfs on it
# 
# Complexity:
# * Time: O(V + E), where V = number of vertices and E = number of edges
# * Space: O(V), for the recursion depth

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../graph/graph.py')


# In[2]:


class GraphDfs(Graph):

    def dfs(self, root, visit_func):
        if root is None:
            return
        visit_func(root)
        root.visit_state = State.visited
        for node in root.adj_nodes.values():
            if node.visit_state == State.unvisited:
                self.dfs(node, visit_func)


# ## Unit Test

# In[3]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[4]:


get_ipython().run_cell_magic('writefile', 'test_dfs.py', 'import unittest\n\n\nclass TestDfs(unittest.TestCase):\n\n    def __init__(self, *args, **kwargs):\n        super(TestDfs, self).__init__()\n        self.results = Results()\n\n    def test_dfs(self):\n        nodes = []\n        graph = GraphDfs()\n        for id in range(0, 6):\n            nodes.append(graph.add_node(id))\n        graph.add_edge(0, 1, 5)\n        graph.add_edge(0, 4, 3)\n        graph.add_edge(0, 5, 2)\n        graph.add_edge(1, 3, 5)\n        graph.add_edge(1, 4, 4)\n        graph.add_edge(2, 1, 6)\n        graph.add_edge(3, 2, 7)\n        graph.add_edge(3, 4, 8)\n        graph.dfs(nodes[0], self.results.add_result)\n        self.assertEqual(str(self.results), "[0, 1, 3, 2, 4, 5]")\n\n        print(\'Success: test_dfs\')\n\n\ndef main():\n    test = TestDfs()\n    test.test_dfs()\n\n\nif __name__ == \'__main__\':\n    main()')


# In[5]:


get_ipython().run_line_magic('run', '-i test_dfs.py')

