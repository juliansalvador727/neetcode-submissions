class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We are given an integer array coins representing different values
        # We are given an integer amount

        # We want to find the lowest number of coins that we need to make up the exact amount
        # If we cannot make the amount, return -1.

        # most naive brute force-y approach

        # lets sort coins, this operation is nlogn time.

        # greedily, we take the highest value v and take smaller values if current + v > target
        # at every v we can chose to take the coin or go to the left one more
        # whenever we take v set target = target - v
        
        # base cases
        # if amount = 0 we cannot construct it since 1 <= coins.length <= 10 OR we have reached our amount
        # if we have 1 coin we can construct amount if and only if target % coin == 0
        # we return target / coin
        
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res,1 + dfs(amount - coin))
            memo[amount] = res
            return res
        mincoin = dfs(amount)
        return -1 if mincoin >= 1e9 else mincoin