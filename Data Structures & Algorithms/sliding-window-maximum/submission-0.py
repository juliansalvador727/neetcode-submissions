import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        res = []

        for i,value in enumerate(nums):
            heapq.heappush(maxheap,(-value,i))

            while maxheap[0][1] <= i - k:
                heapq.heappop(maxheap)
            
            # if our heap is full record the value
            if i >= k - 1:
                res.append(-maxheap[0][0])

        return res