class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0, 1, 2]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n+1):
            stairs.append(stairs[i-1] + stairs[i-2])
        print(stairs)
        return stairs[n]