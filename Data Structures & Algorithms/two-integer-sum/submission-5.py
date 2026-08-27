class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_hash = {}
        for i, num in enumerate(nums):
            target_hash[target - num] = i
        
        for i, num in enumerate(nums):
            if num in target_hash and i != target_hash[num]:
                return [i, target_hash[num]] 
        
        return []


        