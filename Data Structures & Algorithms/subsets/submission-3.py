class Solution:
    output = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.backTrack(nums, subsets)
        subsets.append([])
        return subsets

    def backTrack(self, nums: List[int], subsets: List[List[int]]):
        if not (len(nums) <= 0 or nums in subsets):
            subsets.append(nums)

            for i in range(len(nums)):
                self.backTrack(nums[:i] + nums[i+1:], subsets)
            


