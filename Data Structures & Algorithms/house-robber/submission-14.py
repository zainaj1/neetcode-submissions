class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base cases i = 0, i = 1
        # i(0) = i(0).val
        # i(1) = i(0) if i(0) > i(1).val

        # General Case
        # i = i-1 if i-1 > i.val + i-2 
        n = len(nums)
        
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        memo = [0] * n
        memo[0] = nums[0]
        memo[1] = memo[0] if memo[0] > nums[1] else nums[1]

        for i in range(2, n):
            memo[i] = memo[i-1] if memo[i-1] > nums[i] + memo[i-2] else nums[i] + memo[i-2]
        
        return memo[-1]