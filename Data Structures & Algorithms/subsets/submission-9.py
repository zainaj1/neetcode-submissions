class Solution:
    output = []
    subs = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subs = []
        self.backTrack(nums, 0, [])
        
        return self.subs

    def backTrack(self, nums: List[int], index: int, subset: List[int]):
        if index >= len(nums):
            self.subs.append(subset.copy())
            return None
        
        # Add case
        subset.append(nums[index])
        self.backTrack(nums, index + 1, subset)

        # Not add case 
        subset.pop()
        self.backTrack(nums, index + 1, subset)

        return None

        

            


