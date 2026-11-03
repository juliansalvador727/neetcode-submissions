from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def dfs(i):
            if i >= len(nums):
                return False
            if i == len(nums)-1:
                return True
            for jump in range(1, nums[i] + 1):
                if dfs(i + jump):
                    return True
            return False

        return dfs(0)