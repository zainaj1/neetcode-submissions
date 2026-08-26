class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArr = (2*n)*[0]

        for i in range(n):
            newArr[i] = nums[i]
            newArr[i+n] = nums[i]
        return newArr