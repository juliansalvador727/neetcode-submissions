from functools import cache

class Solution:

    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        t0 = 0
        t1 = 1
        t2 = 1

        for i in range(n-2):
            temp = t2
            t2 = t2 + t1 + t0
            temp1 = t1
            t1 = temp
            t0 = temp1

        return t2