class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        # lets do two passes
        # first pass
        # at treasure chest, append to q
        # apply multi bfs
        # maintain a visited set
        # if we reach a grid[r][c] with inf set that to prev grid value + 1
        # and add to visited set so bfs doesnt visit twice
        # everything in place

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2**31 - 1
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        while q:
            row, cell, step = q.popleft()

            for dx, dy in directions:
                x = row + dx
                y = cell + dy

                if (0 <= x < rows and 0 <= y < cols and grid[x][y] == INF):
                    grid[x][y] = grid[row][cell] + 1
                    q.append((x, y, step + 1))

        


