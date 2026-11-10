class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force
        """
        res = 0
        n = len(height)
        left_max = 0
        for i in range(n):
            left_max = right_max = height[i]
            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i+1, n):
                right_max = max(right_max, height[j])
            res += min(left_max,right_max) - height[i]
        return res
        """
            
        # prefix and suffix array
        """
        res = 0
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = height[0]

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])

        suffix[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        res = 0
        for i in range(n):
            res += min(prefix[i],suffix[i]) - height[i]
        return res
        """
        # stack
        """
        n = len(height)
        if n == 0:
            return 0

        stack = []
        res = 0

        for i in range(n):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res
        """

        # two pointers

        n = len(height)

        if n == 0:
            return 0
        l = 0
        r = n - 1
        res = 0

        left_max, right_max = height[l], height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res
            

