from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        directions = [(0,1),(1,0)] # move right or move down
        @cache
        def dfs(i,j):
            if i == m-1 and j == n-1:
                return 1
            total = 0
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n:
                    total += dfs(x,y)

            return total


        return dfs(0,0)