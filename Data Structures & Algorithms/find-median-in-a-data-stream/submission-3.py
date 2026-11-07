class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.n += 1

    def findMedian(self) -> float:
        n = self.n
        if n == 0:
            return 0 
        if n == 1:
            return self.arr[0]
        if n == 2:
            return (self.arr[0] + self.arr[1]) / 2
        self.arr = sorted(self.arr)

        if n % 2 == 0:
            return (self.arr[n//2] + self.arr[n//2 - 1]) / 2
        else:
            return self.arr[n//2]