class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base cases i = 0, i = 1
        # i(0) = i(0).val
        # i(1) = i(0) if i(0) > i(1).val

        # General Case
        # i = i-1 if i-1 > i.val + i-2 
        
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        memo = [0] * len(nums)
        memo[-1] = nums[-1]
        memo[-2] = memo[-1] if memo[-1] > nums[-2] else nums[-2] # I dont know if this needs to be a base case

        for i in range(len(nums)-3, -1, -1):
            memo[i] = memo[i+1] if memo[i+1] > nums[i] + memo[i+2] else nums[i] + memo[i+2]

        return memo[0]