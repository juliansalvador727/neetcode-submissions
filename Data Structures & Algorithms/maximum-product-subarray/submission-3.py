class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # my observations
        # the lower bound will always be max(nums)
        # if we take max(nums) we aren't multiplying any numbers together
        # product is something we just store, we need to compute the value of each subarray
        # subarrays can be formed by combining sub-subarrays
        # the smallest subarray is size 1, with whatever value that number has
        # when we combine to subarrays, its the same as just having a singular value in the array
        # and that value is subarray1 * subarray2
        # we can do 2d dp on this
        # keep a matrix dp[i][j]
        # dp[i][j] stores the product of the arr[i:j+1]
        # the diagonaal of dp[i][j] is the values in nums


        # 2 x x x
        # x 4 x x
        # x x -3 x
        # x x x 5
        
        # 2 8 -24 -120
        # x 4 -12  -60
        # x x -3   -15
        # x x  x     5

        # n = len(nums)
        # dp = [[0] * n for _ in range(n)]
        # maxprod = -1e8
        # for i in range(n):
        #     dp[i][i] = nums[i] # our base cases
        #     maxprod = max(maxprod, nums[i])
        # for i in range(n):
        #     for j in range(i+1, n):
        #         dp[i][j] = dp[i][j-1] * nums[j]
        #         maxprod = max(maxprod, dp[i][j])
        # return maxprod

        ans = nums[0]
        curmin = curmax = 1
        for num in nums:
            oldcurmax = curmax*num
            curmax = max(num * curmax, num * curmin, num)
            curmin = min(oldcurmax, num*curmin, num)
            ans = max(ans, curmax)
        return ans
        