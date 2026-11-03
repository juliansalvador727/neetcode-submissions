from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i, j):
            if i == len(nums):
                return 0
            skip = dfs(i + 1, j)
            if j == -1 or nums[j] < nums[i]:
                return max(skip, 1+dfs(i+1, i))
            return skip
        return dfs(0, -1)