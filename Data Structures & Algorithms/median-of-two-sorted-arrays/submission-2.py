class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        n = len(nums1)
        m = len(nums2)

        median1 = median2 = 0

        for _ in range((n+m) // 2 + 1):
            median2 = median1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < n:
                median1 = nums1[i]
                i += 1
            elif j < m:
                median1 = nums2[j]
                j += 1
        if (n+m) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2)  / 2.0
