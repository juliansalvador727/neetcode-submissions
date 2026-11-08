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
        copies = defaultdict()
        copy = Node(node.val)
        copies[node] = copy
        q = deque([node])
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                copies[cur].neighbors.append(copies[neighbor])

        return copies[node]