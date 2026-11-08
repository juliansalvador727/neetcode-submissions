class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                    if grid[r][c] == "1":
                        q = deque([(r, c)])
                        grid[r][c] = "0"
                        islands += 1
                        while q:
                            row, col = q.popleft()
                            grid[r][c] = "0"
           
                            for dx, dy in directions:
                                x = row + dx
                                y = col + dy

                                if (0 <= x < rows and 0 <= y < cols and grid[x][y]=="1"):
                                    q.append((x, y))
                                    grid[x][y] = "0"
                                    
        return islands