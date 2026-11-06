from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # recurrence
        # option 1: skip the current day
        # option 2: buy the current day, need to skip the next day.
        memo = {}
        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[i][buying]
            
            cooldown = dfs(i+1,buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            return memo[(i, buying)]


        return dfs(0, True)