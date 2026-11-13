class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # find servers that communicate on same row
        # find servers that communicate on same col

        res = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            sum_row = sum(grid[r])
            if sum_row <= 1:
                continue
            res += sum_row
            for c in range(cols):
                if grid[r][c]:
                    grid[r][c] = -1
        
        # Cols
        for c in range(cols):
            col_sum = 0
            unmarked = 0
            for r in range(rows):
                col_sum += abs(grid[r][c])
                if grid[r][c] > 0:
                    unmarked += 1
                elif grid[r][c] < 0:
                    grid[r][c] = 1
            if col_sum >= 2:
                res += unmarked
        
        return res