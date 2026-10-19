class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # naive solution
        n = len(nums1)
        m = len(nums2)

        n1n2 = nums1 + nums2
        n1n2.sort()

        total = n+m
        if total % 2 == 0:
            return (n1n2[total // 2 - 1] + n1n2[total // 2]) / 2.0
        else:
            return n1n2[total // 2]