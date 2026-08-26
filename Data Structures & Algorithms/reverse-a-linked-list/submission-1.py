class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        previous = None
        curr = head
        next_val = curr.next
        curr.next = previous

        while next_val:
            previous = curr
            curr = next_val
            next_val = curr.next

            curr.next = previous
        
        return curr



# [0,1,2,3]

# [0] -> [1] -> [2] -> [3]

# previous = [0]
# curr = [1]


# next = [2]
# curr.next = [0]

# None <- [0] <- [1] -> [2] -> [3]
