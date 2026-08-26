# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    """
    Given array of k linked lists (lists) return a sorted merged list
    Each list in lists is sorted in ascending order

    Keys:
    1. Working with linkedlists
    2. Merging sorted lists
    3. Lists are sorted in ascending order 

    Solution:
    I will break this problem into three sub problems
    1. Merge sort
        a. How to break the problem into sub problems.
        b. Mainly used for efficency as we can do the problem in nlogn
    2. Merging sorted lists
        a. Sub problem, how do you join two sorted lists
    3. Linked Lists
        a. Traversing linked lists.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length < 1:
            return None
        elif length == 1:
            return lists[0]
        
        m = length//2
        left_list, right_list = self.mergeKLists(lists[0:m]), self.mergeKLists(lists[m:])
        return self.mergeList(left_list, right_list)
    
    """
    Combine the logic of merge 2 sorted arrays with linked list traversal
    [[1,2,4],[1,3,5],[3,6]]
    m = 3//2 = 1
    left_list = [0:1] = [1,3,5]
    right_list = [1, ] = [3,6]
    
    Merge: 
    left_list.: 
    right_list: [6]
    curr......: [1] -> [3] -> *[3] -> [5]
    """
    def mergeList(self, leftList: Optional[ListNode], rightList: Optional[ListNode]) -> Optional[ListNode]:
        
        # validate if the lists are defined
        if not leftList:
            return rightList
        elif not rightList:
            return leftList
        
        if leftList.val <= rightList.val:
            curr = leftList
            leftList = leftList.next
        else:
            curr = rightList
            rightList = rightList.next

        head = curr
        
        while leftList and rightList:
            if leftList.val <= rightList.val:
                curr.next = leftList
                leftList = leftList.next
            else:
                curr.next = rightList
                rightList = rightList.next
            curr = curr.next
        
        if rightList:
            curr.next = rightList
        elif leftList:
            curr.next = leftList
        
        return head
        

         

        
        