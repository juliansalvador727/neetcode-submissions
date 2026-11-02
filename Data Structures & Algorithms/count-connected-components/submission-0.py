class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # return the number of representatives
        num_rep = n
        size = [1] * n

        parent = list(range(n))

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a,b):
            u = find(a)
            v = find(b)

            if u == v:
                return False
            if size[u] <= size[v]:
                u,v = v,u
            parent[v] = u
            size[u] += size[v]
            return True
        
        for a, b in edges:
            if union(a,b):
                num_rep -= 1
        return num_rep
