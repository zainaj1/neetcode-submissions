"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        visited = {}
        queue = deque()
        queue.append(node)
        
        while queue:
            node = queue.popleft()
            if not node.val in visited:
                curr = Node(node.val)
                visited[node.val] = curr
            else:
                curr = visited[node.val]

            neighbors = []
            for neighbor in node.neighbors:
                if neighbor.val in visited:
                    new_node = visited[neighbor.val]
                else:
                    new_node = Node(neighbor.val)
                    visited[neighbor.val] = new_node
                    queue.append(neighbor)
                
                neighbors.append(new_node)
            
            curr.neighbors = neighbors
            
        return visited[1]

        