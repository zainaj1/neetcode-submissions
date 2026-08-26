class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for num in nums:
            if num in numMap:
                return True
            
            numMap[num] = 1
        
        return False

        # for i in range(0, len(nums)-1):
        #     if(nums[i] > 0):
        #         return True

        # return False
# [1, 2, 3, 4]
# [-1, -2, -3, -4]
        