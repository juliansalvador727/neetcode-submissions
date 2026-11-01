class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), [0, -1]]
        rows, cols = len(grid), len(grid[0])
        max_islands = 0

        st = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    st.append((r, c))

                    islands = 1

                    while st:
                        row, col = st.pop()

                        for dx, dy in directions:
                            x = row + dx
                            y = col + dy

                            if (0 <= x < rows and 0 <= y < cols and grid[x][y] == 1):
                                grid[x][y] = 0
                                st.append((x,y))
                                islands += 1
                    max_islands = max(max_islands, islands)

        return max_islands