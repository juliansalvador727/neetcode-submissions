class MedianFinder:

    def __init__(self):
        #lo for lower half - smaller elements
        #lo for upper half - larger elements
        #we want root of both to calculate median
        self.hi, self.lo = [], []

    def addNum(self, num: int) -> None:
        if self.lo and num > -self.lo[0]:
            heapq.heappush(self.hi, num)
        else:
            heapq.heappush(self.lo, -1 * num)
        
        # rebalance
        if len(self.hi) > len(self.lo) + 1:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))


    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -1 * self.lo[0]
        elif len(self.hi) > len(self.lo):
            return self.hi[0]
        return (-1 * self.lo[0] + self.hi[0]) / 2.0
        