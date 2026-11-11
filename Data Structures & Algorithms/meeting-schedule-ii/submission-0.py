"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        active_ends = []
        rooms = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            while active_ends and active_ends[0] <= start:
                heapq.heappop(active_ends)
            heapq.heappush(active_ends, end)
            rooms = max(rooms, len(active_ends))
        return rooms