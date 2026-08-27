class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_hash = {}
        i = 0
        while nums[i] not in target_hash:
            target_hash[target - nums[i]] = i
            i+=1
        
        return [target_hash[nums[i]], i]
        