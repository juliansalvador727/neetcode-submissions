class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(bin(n))[2:][::-1] + "0" * (32 - len(str(bin(n))[2:])),2)