class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2

            totaltime = 0
            for p in piles:
                totaltime += math.ceil(float(p) / mid)
            if totaltime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res