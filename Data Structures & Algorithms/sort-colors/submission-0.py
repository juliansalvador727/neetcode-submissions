class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            elif n == 2:
                blue += 1
        
        i = 0
        while (red):
            nums[i] = 0
            red-=1
            i+=1
        while(white):
            nums[i]=1
            white-=1
            i+=1
        while(blue):
            nums[i]=2
            blue-=1
            i+=1
