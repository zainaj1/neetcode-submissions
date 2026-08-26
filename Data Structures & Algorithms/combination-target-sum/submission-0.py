class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_sums = []
        
        self.backTrackSum(0, 0, [], all_sums, nums, target)
        return all_sums
    
    def backTrackSum(self, index, total, sums, all_sums, nums, target):
        if index >= len(nums) and total != target:                
            return 
        
        if total > target:
            return
        
        if total == target:
            all_sums.append(sums.copy())
            return
        
        total += nums[index]
        sums.append(nums[index])

        # Add case same value
        self.backTrackSum(index, total, sums, all_sums, nums, target)

        # # Add case
        # self.backTrackSum(index + 1, total, sums, all_sums, nums, target)
        
        # Dont add case
        total -= nums[index]
        sums.pop()
        self.backTrackSum(index + 1, total, sums, all_sums, nums, target)
        
        return 




    
         