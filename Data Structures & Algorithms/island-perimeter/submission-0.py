class Solution:
    def getPerim(self, r, c, rows, cols, grid):
        perim = 4
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dx, dy in directions:
            x = dx + r
            y = dy + c

            if (0 <= x < rows and 0 <= y < cols and grid[x][y] == 1):
                perim -= 1

        return perim


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        perim = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
                    break

        while q:
            r, c = q.popleft()
            visited.add((r, c))
            perim += self.getPerim(r, c, rows, cols, grid)

            for dx, dy in directions:
                x = r + dx
                y = c + dy
                if (0 <= x < rows and 0 <= y < cols and grid[x][y] == 1 and (x,y) not in visited):
                    q.append((x, y))
                    visited.add((x, y))
        return perim
            


