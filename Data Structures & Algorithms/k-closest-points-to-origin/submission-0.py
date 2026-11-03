import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(x**2 + y**2, i) for i, (x,y) in enumerate(points)]

        heapq.heapify(distance)

        results = []
        for _ in range(k):
            d, i = heapq.heappop(distance)
            results.append(points[i])
        return results