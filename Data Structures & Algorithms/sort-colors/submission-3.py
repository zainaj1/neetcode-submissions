class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colours = [0, 0, 0]
        for i in range(len(nums)):
            colours[nums[i]] += 1 
        

        colour = 0
        for i in range(len(nums)):
            while colours[colour] <= 0:
                colour += 1

            nums[i] = colour
            colours[colour] -= 1         
        