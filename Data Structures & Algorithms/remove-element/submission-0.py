class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i in range (len(nums)-1, -1, -1):
            if(nums[i] == val):
                for j in range(i, k-1):
                    nums[j] = nums[j+1]
                k = k-1
        return k
        