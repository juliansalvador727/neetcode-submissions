class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        parent = list(range(n))
        size = [1] * (n)
        
        directions = [(1,0),(0,1)]

        def find(cell):
            while cell != parent[cell]:
                parent[cell] = parent[parent[cell]]
                cell = parent[cell]
            return cell
        
        def union(a, b):
            u, v = find(a), find(b)
            if u == v:
                return False
            if size[u] <= size[v]:
                u, v = v, u
            parent[v] = u
            size[u] += size[v]
            return True
        
        def index(i, j):
            return i * cols + j

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    for dx, dy in directions:
                        x = dx + r
                        y = dy + c

                        if (0 <= x < rows and 0 <= y < cols and grid[x][y] == 1):
                            union(index(x,y),index(r,c))

                    max_area = max(max_area, size[find(index(r,c))])

        return max_area