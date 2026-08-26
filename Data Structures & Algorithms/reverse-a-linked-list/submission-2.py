class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr: 
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        return prev # We return prev becuase it stores the last curr value before we reached the next of the list 

    
    # iteration: 
    # list:
    # null
    # [1] -> null
    # [1] -> [2] -> null
    # [1] -> [2] -> [3] -> null
    # 1_0, curr: [1], prev: null, next_node:?, linkedList: [1] -> [2] -> null
    # 1_1, curr: [2], prev: [1], next_node:[2], linkedList: [1] -> null, [2] -> null
    # 2_0, curr: [2], prev: [1], next_node:[2], linkedList: [1] -> null, [2] -> null
    # 2_1, curr: null, prev: [2], next_node:null, linkedList: [2] -> [1] -> null,
    # 3_0
    # 3_1
        

    

