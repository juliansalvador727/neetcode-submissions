from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        @cache
        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            choose = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    choose = max(choose, 1 + dfs(j))
            memo[i] = choose
            return choose
        return max(dfs(i) for i in range(len(nums)))