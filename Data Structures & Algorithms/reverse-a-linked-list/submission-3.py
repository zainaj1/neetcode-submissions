

"""
Here we are taking advantage of the fact that linked lists are based on pointers (1), and the fact that recursive funtions, resolve
from inner most call to outer call, which means f(n-1) will resolve before f(n) (2). Now with these two properties in mind what we essentially do
is for each call we reverse the order and detach the current head, then call our recursive function on the next node. 

For each iteration i, let node_i be the current node (aka head), where node_i+1 is the the next node in the list (before the reverse)

If we call f(i+1) then set node_(i+1)+1.next to node_(i+1), and then set node_(i+1).next to None,   

Due to property (1), we know that node_i+1 is is the same pointer as to node_i.next for f(i)  
Due to property (2), we know that setting node_(i)+1.next to node_i, and then set node_i.next to None happens after f(i+1) resolves

i.e 
node_i+1 = node_i.next and node_i+2.next = node_i+1 and node_(i+1).next = None    

then in f(i) we doing the following:
node_i+1.next = node_i, and node_i.next = None,

since node_i+1.next is set to node_i in f(i) after we set node_i+1.next = None in f(i+1) due to property 2 we know that node_i+1 is continus.




In a recursive call we need to keep track of the start of the iteration and the end, as well as the sequence of events 
0 -> 1 -> 2 -> 3 -> None
0: 1 -> 0, 0 -> None, reverseList(1)
1: 2 -> 1, 1 -> None, reverseList(2) 
2: 3 -> 2, 2 -> None, reverseList(3)
3: 4 -> 3, 3 -> None, reverseList(4)
4: 4
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif head.next is None:
            return head
        
        # reverse and detach
        curr = self.reverseList(head.next)

        next_node = head.next 
        next_node.next = head 
        head.next = None

        return curr





    

 