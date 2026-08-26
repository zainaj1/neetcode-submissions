class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
       

        # If our mid is greater then the target then we know everything to the right of it would be greater too, same with if mid was less than target 
        # then everything to the left of it would be less too
        while l <= r: # Include the equal for the case where mid == l == r 
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1 # we do +1 because mid was already checked, you could just do mid but its including extra elements we dont need
            else:
                r = mid - 1  
        
        return -1
        