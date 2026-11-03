class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []


        for num in range(n+1):
            total = 0
            while num:
                num &= num - 1
                total += 1
            ans.append(total)
        return ans
