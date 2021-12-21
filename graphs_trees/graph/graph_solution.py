#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a graph.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the graph directed?
#     * Implement both
# * Do the edges have weights?
#     * Yes
# * Can the graph have cycles?
#     * Yes
# * If we try to add a node that already exists, do we just do nothing?
#     * Yes
# * If we try to delete a node that doesn't exist, do we just do nothing?
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
# graph.add_edge(0, 5, 2)
# graph.add_edge(1, 2, 3)
# graph.add_edge(2, 3, 4)
# graph.add_edge(3, 4, 5)
# graph.add_edge(3, 5, 6)
# graph.add_edge(4, 0, 7)
# graph.add_edge(5, 4, 8)
# graph.add_edge(5, 2, 9)
# ```
# 
# Result:
# * `source` and `destination` nodes within `graph` are connected with specified `weight`.
# 
# Note: 
# * The Graph class will be used as a building block for more complex graph challenges.

# ## Algorithm
# 
# ### Node
# 
# Node will keep track of its:
# * id
# * visit state
# * incoming edge count (useful for algorithms such as topological sort)
# * adjacent nodes and edge weights
# 
# #### add_neighbor
# 
# * If the neighbor doesn't already exist as an adjacent node
#     * Update the adjacent nodes and edge weights
#     * Increment the neighbor's incoming edge count
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# #### remove_neighbor
# 
# * If the neighbor exists as an adjacent node
#     * Decrement the neighbor's incoming edge count
#     * Remove the neighbor as an adjacent node
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Graph
# 
# Graph will keep track of its:
# * nodes
# 
# #### add_node
# 
# * If node already exists, return it
# * Create a node with the given id
# * Add the newly created node to the collection of nodes
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# #### add_edge
# 
# * If the source node is not in the collection of nodes, add it
# * If the dest node is not in the collection of nodes, add it
# * Add a connection from the source node to the dest node with the given edge weight
# 
# #### add_undirected_edge
# 
# * Call add_edge
# * Also add a connection from the dest node to the source node with the given edge weight
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'graph.py', "from enum import Enum  # Python 2 users: Run pip install enum34\n\n\nclass State(Enum):\n\n    unvisited = 0\n    visiting = 1\n    visited = 2\n\n\nclass Node:\n\n    def __init__(self, key):\n        self.key = key\n        self.visit_state = State.unvisited\n        self.incoming_edges = 0\n        self.adj_nodes = {}  # Key = key, val = Node\n        self.adj_weights = {}  # Key = key, val = weight\n\n    def __repr__(self):\n        return str(self.key)\n\n    def __lt__(self, other):\n        return self.key < other.key\n\n    def add_neighbor(self, neighbor, weight=0):\n        if neighbor is None or weight is None:\n            raise TypeError('neighbor or weight cannot be None')\n        neighbor.incoming_edges += 1\n        self.adj_weights[neighbor.key] = weight\n        self.adj_nodes[neighbor.key] = neighbor\n\n    def remove_neighbor(self, neighbor):\n        if neighbor is None:\n            raise TypeError('neighbor cannot be None')\n        if neighbor.key not in self.adj_nodes:\n            raise KeyError('neighbor not found')\n        neighbor.incoming_edges -= 1\n        del self.adj_weights[neighbor.key]\n        del self.adj_nodes[neighbor.key]\n\n\nclass Graph:\n\n    def __init__(self):\n        self.nodes = {}  # Key = key, val = Node\n\n    def add_node(self, key):\n        if key is None:\n            raise TypeError('key cannot be None')\n        if key not in self.nodes:\n            self.nodes[key] = Node(key)\n        return self.nodes[key]\n\n    def add_edge(self, source_key, dest_key, weight=0):\n        if source_key is None or dest_key is None:\n            raise KeyError('Invalid key')\n        if source_key not in self.nodes:\n            self.add_node(source_key)\n        if dest_key not in self.nodes:\n            self.add_node(dest_key)\n        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)\n\n    def add_undirected_edge(self, src_key, dst_key, weight=0):\n        if src_key is None or dst_key is None:\n            raise TypeError('key cannot be None')\n        self.add_edge(src_key, dst_key, weight)\n        self.add_edge(dst_key, src_key, weight)")


# In[2]:


get_ipython().run_line_magic('run', 'graph.py')


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_graph.py', "import unittest\n\n\nclass TestGraph(unittest.TestCase):\n\n    def create_graph(self):\n        graph = Graph()\n        for key in range(0, 6):\n            graph.add_node(key)\n        return graph\n\n    def test_graph(self):\n        graph = self.create_graph()\n        graph.add_edge(0, 1, weight=5)\n        graph.add_edge(0, 5, weight=2)\n        graph.add_edge(1, 2, weight=3)\n        graph.add_edge(2, 3, weight=4)\n        graph.add_edge(3, 4, weight=5)\n        graph.add_edge(3, 5, weight=6)\n        graph.add_edge(4, 0, weight=7)\n        graph.add_edge(5, 4, weight=8)\n        graph.add_edge(5, 2, weight=9)\n\n        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)\n        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)\n        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)\n        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[3].key], 4)\n        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[4].key], 5)\n        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[5].key], 6)\n        self.assertEqual(graph.nodes[4].adj_weights[graph.nodes[0].key], 7)\n        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[4].key], 8)\n        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[2].key], 9)\n\n        self.assertEqual(graph.nodes[0].incoming_edges, 1)\n        self.assertEqual(graph.nodes[1].incoming_edges, 1)\n        self.assertEqual(graph.nodes[2].incoming_edges, 2)\n        self.assertEqual(graph.nodes[3].incoming_edges, 1)\n        self.assertEqual(graph.nodes[4].incoming_edges, 2)\n        self.assertEqual(graph.nodes[5].incoming_edges, 2)\n\n        graph.nodes[0].remove_neighbor(graph.nodes[1])\n        self.assertEqual(graph.nodes[1].incoming_edges, 0)\n        graph.nodes[3].remove_neighbor(graph.nodes[4])\n        self.assertEqual(graph.nodes[4].incoming_edges, 1)\n\n        self.assertEqual(graph.nodes[0] < graph.nodes[1], True)\n\n        print('Success: test_graph')\n\n    def test_graph_undirected(self):\n        graph = self.create_graph()\n        graph.add_undirected_edge(0, 1, weight=5)\n        graph.add_undirected_edge(0, 5, weight=2)\n        graph.add_undirected_edge(1, 2, weight=3)\n\n        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)\n        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[0].key], 5)\n        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)\n        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[0].key], 2)\n        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)\n        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[1].key], 3)\n\n        print('Success: test_graph_undirected')\n\n\ndef main():\n    test = TestGraph()\n    test.test_graph()\n    test.test_graph_undirected()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_graph.py')

