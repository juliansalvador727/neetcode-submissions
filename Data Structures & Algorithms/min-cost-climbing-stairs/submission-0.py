class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we are given an array of integers cost
        # cost[i] is the cost of taking a step from the ith floor of the staircase
        # after you pay the cost you can step to either (i+1) or (i+2) floor
        # you may choose to start at index 0 or index 1

        # define dp[i] = the minimum cost to reach position i, before paying for that step.
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]