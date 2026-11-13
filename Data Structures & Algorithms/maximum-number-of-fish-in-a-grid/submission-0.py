class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols))
        size = [fish for row in grid for fish in row]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def find(cell):
            while cell != parent[cell]:
                parent[cell] = parent[parent[cell]]
                cell = parent[cell]
            return cell
        
        def union(a, b):
            u,v = find(a), find(b)
            if u == v:
                return False
            if u < v:
                u,v = v,u
            parent[v] = u
            size[u] += size[v]
            return True

        def at(r, c):
            return r * cols + c
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x, y = r + dx, c + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] > 0:
                        union(at(r,c),at(x,y))
                    


        return max(size)