class Solution:
    def reverseBits(self, n: int) -> int:
        length = 34 - len(bin(n))
        s = str(bin(n))
        s = s[2:]
        s = s[::-1]
        s += "0" * length
        

        return int(s,2)