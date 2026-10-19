class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 9999
        for n in nums:
            ans = min(ans, n)
        return ans