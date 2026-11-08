class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        parent = list(range(n+1))
        size = [1] * (n+1)


        def find(cell):
            while cell != parent[cell]:
                parent[cell] = parent[parent[cell]]
                cell = parent[cell]
            return cell
        
        def union(a, b):
            u = find(a)
            v = find(b)

            if u == v:
                return False
            if size[u] <= size[v]:
                u, v = v, u
            parent[v] = u
            size[u] += size[v]
            return True
        
        def index(r, c):
            return r * cols + c
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    for dx, dy in directions:
                        x = r + dx
                        y = c + dy

                        if (0 <= x < rows and 0 <= y < cols and grid[x][y] == "1"):
                            if union(index(r,c), index(x, y)):
                                islands -= 1
        return islands
        
