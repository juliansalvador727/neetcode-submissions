class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx, n in enumerate(nums):
            if n == target:
                return idx
        return -1