class Solution:
    output = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.backTrack(nums, subsets)
        subsets.append([])
        return subsets

    def backTrack(self, nums: List[int], subsets: List[List[int]]) -> bool:
        if len(nums) <= 0 or nums in subsets:
            return False
        
        subsets.append(nums)

        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            self.backTrack(nums_copy, subsets)
        
        return True



