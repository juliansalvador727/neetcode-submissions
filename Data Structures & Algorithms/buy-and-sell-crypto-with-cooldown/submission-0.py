from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # recurrence
        # option 1: skip the current day
        # option 2: buy the current day, need to skip the next day.

        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i+1,buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                return max(sell, cooldown)


        return dfs(0, True)