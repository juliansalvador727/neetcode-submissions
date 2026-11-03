class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for (a,b), value in zip(equations, values):
            adj[a].append((b, value))
            adj[b].append((a, 1/value))

        def bfs(a, b):
            if a not in adj or b not in adj:
                return -1.0
            q = deque([(a, 1.0)])
            visited = set()
            visited.add(a)

            while q:
                val, cur = q.popleft()

                if val == b:
                    return cur

                for neighbor, weight in adj[val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, cur*weight))

            return -1.0 
        
        ans = [-1.0] * len(queries)
        for i, (a,b) in enumerate(queries):
            value = bfs(a,b)
            ans[i] = value if value != -1.0 else -1.0
        
        return ans

                