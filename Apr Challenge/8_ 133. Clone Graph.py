# problem:
# https://leetcode.com/problems/clone-graph/

# solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        visited = {}
        
        def clone(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]
            
            copy = Node(node.val)
            visited[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy 
        
        return clone(root) if root else None