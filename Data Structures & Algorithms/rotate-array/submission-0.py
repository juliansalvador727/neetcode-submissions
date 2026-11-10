class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k %= n
        def reverse_nums(a, b):
            while a < b:
                nums[a],nums[b] = nums[b],nums[a]
                a+=1
                b-=1
            return
        reverse_nums(0, n-1)
        reverse_nums(0, k-1)
        reverse_nums(k, n-1)