"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew= {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            # Append copy as old <-> new
            copy = Node(node.val)
            oldToNew[node] = copy

            # Recurse dfs on each neighbor of the node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            # return copy
            return copy
        
        return dfs(node) if node else None