class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        def backtrack(i, remaining):
            if remaining == 0:
                results.append(path.copy())
                return
            if i >= len(nums) or remaining < 0:
                return
            path.append(nums[i])
            backtrack(i, remaining - nums[i])
            path.pop()
            backtrack(i + 1, remaining)

        backtrack(0, target)
        return results