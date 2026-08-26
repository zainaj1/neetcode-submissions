class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,41], n = 2

        nums1 = [10,20,20,40,40,41]

        I think the intuition here is that we know in our final list the last emlement will be the largest and that the array will go backwords in decending order.
        This lets us build the list backworks by going thorugh both lists and putting the largest element there.

        Now the problem is once we pull n elements in nums1 we will have to start modifying m elements in nums1 so how do we garauntee correctness.
        Intuitively we can assume there will always be a buffer of n-i elements (where i is the number of elements inserted from n)
        
        This is because the buffer at the end is n elements long, if we add an element from nums1 we just shift the buffer down, if we add an element from nums2
        we decrease the buffer by one, since the buffer is the same size of n the buffer only goes away when we add all the elements from nums2.

        We use the analogy of shifting the buffer down since the elemnts added from nums1 border the buffer. I.e starting at element m going backwords. If
        we add an element to the list then its spot no longer matters, since it boarded the buffer we can now treat the items old positin as the new start to our
        buffer since its duplicated now. Hence the element we look at in nums1 is always the element immedietly preceding the buffer.
        """

        i = m - 1
        j = n - 1
        index = (m+n)-1

        while j >= 0 and i >= 0 and index >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1 
            else:
                nums1[index] = nums2[j]
                j -=1
            index -= 1
        

        while j >= 0:
            nums1[index] = nums2[j]
            j-=1
            index -= 1
    
                 
                 


        