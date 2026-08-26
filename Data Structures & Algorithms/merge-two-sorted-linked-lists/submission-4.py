# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
I Think the solution to this is to just insert one element at a time from list 1 into list 2
Since the lists are sorted we can just keep the pointer where it is, as long as the curr value is less then the curr value of list 2, we keep inserting

Sample:
list1=[1,2,4]
list2=[1,3,5]

curr1: 2
curr2: 3
prev2: 1
temp: 2

list2=[1,1,3,5]
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Ensure our list is always populated 
        if not list1:
            return list2
        elif not list2:
            return list1
        
        curr1 = list1 if list1.val >= list2.val else list2
        curr2 = list2 if list1.val >= list2.val else list1

        prev1 = None
        prev2 = None

        # Insert a node from list 1 into list2 every time that node is smaller then the pointer in list2
        while curr1:
            while curr2 and curr1.val >= curr2.val:
                prev2 = curr2
                curr2 = curr2.next
            
            temp = curr1.next
            prev1 = curr1
            if prev2:
                self.insert(prev2, curr1)
                prev2 = curr1
            curr1 = temp

        if not prev2:
            prev1.next = list2

        return list1 if list1.val < list2.val else list2
    
    def insert(self, prevNode: ListNode, insertNode: ListNode):
        insertNode.next = prevNode.next
        prevNode.next = insertNode





