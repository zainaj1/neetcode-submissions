class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = {}
        for num in nums:
            if num in seen_nums:
                return True
            seen_nums[num] = 1
        return False
