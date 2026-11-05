class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        l = 0
        r = n - 1
        left_max,right_max = height[l],height[r]
        res = 0

        while l < r:
            if left_max<right_max:
                l+=1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res