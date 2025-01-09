# The cloneGraph method creates a deep copy of a graph using DFS or BFS.

# DFS Approach:
# - Use a dictionary `oldToNew` to map original nodes to their copies.
# - Traverse the graph recursively, copying nodes and their neighbors.

# BFS Approach:
# - Use a queue to traverse nodes level by level.
# - For each node, create its copy if not already in `oldToNew` and enqueue its neighbors.
# - Link the copied neighbors to the copied node.

# TC: O(V + E) - Traverse all nodes (V) and edges (E).
# SC: O(V) - Space for the mapping dictionary and recursion/queue.



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from xml.dom import Node
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        # DFS Approach

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)

        # BFS Approach

        queue = deque([node])

        oldToNew[node] = Node(node.val)

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in oldToNew:
                 
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
             
                oldToNew[current].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]
