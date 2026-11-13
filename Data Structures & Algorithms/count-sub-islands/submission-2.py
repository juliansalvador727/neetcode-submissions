class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 0 or grid2[r][c] == 2:
                    continue
                q = deque()
                # mark as visited
                grid2[r][c] = 2
                q.append((r, c))
                flag = 1
                while q:
                    row, col = q.popleft()
                    if grid1[row][col] == 0:
                        flag = 0
                    for dx, dy in directions:
                        x, y = row + dx, col + dy

                        if 0 <= x < rows and 0 <= y < cols and grid2[x][y] == 1:
                            q.append((x, y))
                            grid2[x][y] = 2

                island += flag
        return island
                    