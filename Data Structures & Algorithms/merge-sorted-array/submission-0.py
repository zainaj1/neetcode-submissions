class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        insertionIndex = 0
        nums1Copy = nums1[0:m].copy()
        while i < m and j < n:
            if nums1Copy[i] <= nums2[j]: 
                nums1[insertionIndex] = nums1Copy[i]
                i+=1
                insertionIndex += 1
            else:
                nums1[insertionIndex] = nums2[j]
                j+=1
                insertionIndex += 1
        
        while i < m:
            nums1[insertionIndex] = nums1Copy[i]
            i+=1
            insertionIndex += 1
        
        while j < n:
            nums1[insertionIndex] = nums2[j]
            j+=1
            insertionIndex += 1

                

        