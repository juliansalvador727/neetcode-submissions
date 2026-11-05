class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since we have a non decreasing order list of numbers
        # and a target number
        # we can perform some optimizations to solve this problem
        # store two pointers l and r.
        # keep l at beginning, r at end
        # if nums[l]+nums[r] < target
        # increment l
        # else if nums[l] + nums[r] > target
        # decrement r
        # otherwise we have found our target and return [l, r]
        # that is the naive implementation which runs in O(n) with O(1) and gurantees an answer 
        # because we are given that

        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            elif total == target:
                return [l+1,r+1]
        
