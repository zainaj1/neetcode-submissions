class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_sums = []
        
        self.backTrackSum(0, 0, [], all_sums, nums, target)
        return all_sums
    
    def backTrackSum(self, index, total, sums, all_sums, nums, target):
        # Add case same value
        if total == target:
            all_sums.append(sums.copy())
            return 
        if index >= len(nums) or total > target:                
            return 
        
        # Add case 
        sums.append(nums[index])
        self.backTrackSum(index, total + nums[index], sums, all_sums, nums, target)
        
        # Dont add case
        sums.pop()
        self.backTrackSum(index + 1, total, sums, all_sums, nums, target)
        
        return 




    
         