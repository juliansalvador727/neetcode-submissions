class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # for each node in our graph
        # also store it as an adjacency list
        # find the height in each node save to heights[height] = root
        # min(heights[height])

        heights = defaultdict(list)

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(node):
            height = 0
            visited = set([node])
            q = deque([(node, 0)])
            while q:
                current, distance = q.popleft()
                height = max(height, distance)
                visited.add(current)

                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, distance + 1))

            return height

        for i in range(n):
            heights[bfs(i)].append(i)
        
        return heights[min(heights)]
