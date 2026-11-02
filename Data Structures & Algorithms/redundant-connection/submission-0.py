class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, a, b):
        u = self.find(a)
        v = self.find(b)

        if u == v:
            return False
        if self.size[u] <= self.size[v]:
            u, v = v, u
        self.parent[v] = u
        self.size[u] += self.size[v]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
        



