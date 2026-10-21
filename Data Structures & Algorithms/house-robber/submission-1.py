class Solution:
    def rob(self, nums: List[int]) -> int:
        # you are given a list nums
        # nums[i] represents the amount of money the ith house has
        # the houses are arranged in a straight line
        # you cannot rob two adjacent houses
        # return the max amount of money you can rob without alerting the police

        # let dp[i] = the max money you can obtain by robbing up to house i
        # at every i, you can chose to rob the current house, or the next house
        # you want the max(current house, next house)
        # so dp[i] = max(current, next)
        # and we know the money you get to rob the 0-th house is nums[0]
        # and to rob the 1st house is nums[1]

        # the most amount of money you can get therefore is the max of dp[n]. dp[n-1].
        n = len(nums)

        if n == 1:
            return nums[0]
        dp = [0] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return max(dp[n], dp[n-1])