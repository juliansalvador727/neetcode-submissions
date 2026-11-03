import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-n for n in nums]

        heapq.heapify(maxheap)

        for _ in range(k-1):
            heapq.heappop(maxheap)
        
        return ---maxheap[0]
