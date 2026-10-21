class Solution:
    def rob(self, nums: List[int]) -> int:
        # you are given an integer array nums
        # nums[i] represents the amount of money the ith house has

        # rules
        # the houses are arranged circularly, i.e. the first and the last house are neighbors
        # you cannot rob two adjacent house

        # at every i we can chose
        # rob (we cannot rob the i+1 house)
        # pass (we have the option to rob the i+1 house)

        # dp[i] = max(dp[i-1], dp[i-2] + cost[i]) <-- cost to rob at i

        # what do we need to consider? we are on a variation of this problem.
        # robbing last house implies you cannot rob the last house.
        # likewise, robbing the last house means you cannot rob the first house.
        # so the cost of robbing the first house is adjusted to be
        # max(cost[i], cost[n-1])?

        # the cost of robbing the last house is also max(cost[i]. cost[n-1])

        # what we can try / what i can think of in terms of naive, brute forcing

        # 3 options:
        # rob first house -> then second house cannot be robbed and last house cannot be robbed -> then continue problem normally
        # rob last house -> then continue problem normally, but first house cannot be robbed, and second last house cannot be robbed
        # pass both first and last house

        if len(nums) == 1:
            return nums[0]


        def houseRobber(houses):
            if len(houses) == 1:
                return houses[0]

            n = len(houses)

            dp = [0] * (n+1)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[n - 1]
        
        return max(houseRobber(nums[1:]), houseRobber(nums[:-1]))





