class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        q = deque()
        
        fresh = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,time))
                if grid[r][c] == 1:
                    fresh += 1
        
        while q:
            row, col, time = q.popleft()

            for dx, dy in directions:
                x = dx + row
                y = dy + col

                if (0 <= x < rows and 0 <= y < cols and grid[x][y] == 1):
                    grid[x][y] = 2
                    fresh -= 1
                    q.append((x, y, time + 1))

        return time if not fresh else -1