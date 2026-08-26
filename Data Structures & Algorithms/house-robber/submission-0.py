class Solution:
    def rob(self, nums: List[int]) -> int:
        results = {}
        return self.rob_rec(nums, 0, results)


    def rob_rec(self, nums: List[int], index, results) -> int:
        if index > len(nums) - 1:
            return 0 
        
        results[index+1] = results[index+1] if index + 1 in results else self.rob_rec(nums, index + 1, results)
        results[index+2] = results[index+2] if index + 2 in results else self.rob_rec(nums, index + 2, results)

        return  max(nums[index] + results[index+2], results[index+1])
        