class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c]==2:
                    q.append((r,c,0))

        minutes = 0
        while q:
            row, col, minutes = q.popleft()
            for dx, dy in directions:
                x = row + dx
                y = col + dy

                if (0 <= x < rows and 0 <= y < cols and grid[x][y] == 1):
                    q.append((x, y, minutes + 1))
                    grid[x][y] = 2
                    fresh -= 1

        

        return minutes if not fresh else -1
                
