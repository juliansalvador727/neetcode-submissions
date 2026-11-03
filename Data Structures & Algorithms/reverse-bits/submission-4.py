class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n))[2:][::-1] + "0" * (32 - len(str(bin(n))[2:]))

        return int(s,2)