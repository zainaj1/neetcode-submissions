class Solution:
    """
    You can notice a property with target
    if nums[i] + nums[j] = target 
    => target - nums[i] = nums[j]

    Since there is only one solution in our input we can assume that there is only one i index that satisfies target - nums[i] = nums[j]
    so what we can do is store target-nums[i] as our key in our hashtable, for the next element if it exists in our hashtable we return 
    the indexes.

    If there is only one solution then only one index i will satisfy target - nums[i] = nums[j]. So for each value we check if its in the map
    if its not in the map we add target - nums[i] and then iterate, eventually we will get to the index that satifies our equation to which we can return 
    the indexs for our solution.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        results = []
        for i in range(len(nums)):
            if nums[i] in sums:
                results = [sums[nums[i]], i]
                break 
            sums[target - nums[i]] = i

        return results
        