class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 0 or grid2[r][c] == 2:
                    continue
                check = []
                q = deque()
                # mark as visited
                grid2[r][c] = 2
                check.append((r, c))
                q.append((r, c))
                while q:
                    row, col = q.popleft()
                    for dx, dy in directions:
                        x, y = row + dx, col + dy

                        if 0 <= x < rows and 0 <= y < cols and grid2[x][y] == 1:
                            check.append((x,y))
                            q.append((x, y))
                            grid2[x][y] = 2

                # now check in grid1
                flag = True
                for x,y in check:
                    if grid1[x][y] == 0:
                        flag = False
                        break
                if flag:
                    island += 1
        return island
                    