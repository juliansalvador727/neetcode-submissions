class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q:
            row, col, value = q.popleft()

            for dx, dy in directions:
                x = row + dx
                y = col + dy

                if (0 <= x < rows and 0 <= y < cols and grid[x][y] == INF):
                    grid[x][y] = value + 1
                    q.append((x, y, value+1))




