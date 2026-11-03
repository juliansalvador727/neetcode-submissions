class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n))
        s = s[2:]
        s = s[::-1]
        s += "0" * (32 - len(str(bin(n))[2:]))
        

        return int(s,2)