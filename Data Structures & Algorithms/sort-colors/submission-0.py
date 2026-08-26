class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colours = [0, 0, 0]
        for i in range(len(nums)):
            colours[nums[i]] += 1 
        
        for i in range(len(nums)):
            if colours[0] > 0:
                nums[i] = 0
                colours[0] -= 1
            elif colours[1] > 0:
                nums[i] = 1
                colours[1] -= 1
            else:
                nums[i] = 2
                colours[2] -= 2            
        