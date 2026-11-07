class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.n += 1

    def findMedian(self) -> float:
        n = self.n
        self.arr = sorted(self.arr)

        if n % 2 == 0:
            return (self.arr[n//2] + self.arr[n//2 - 1]) / 2
        else:
            return self.arr[n//2]