class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def enqueue(self, val):
        new_node = QueueNode(val)
        if self.end:
            self.end.next = new_node
            self.end = new_node
        else:
            self.start = self.end = new_node
        
    
    def dequeue(self):
        if not self.start:
            return None
        
        val = self.start.val
        self.start = self.start.next

        if not self.start:
            self.end = None
        
        return val

"""
we want LIFO (the newest element is returned first)
we have FIFO (the oldest element is returned first)

In our case we have two FIFO queues, so to get LIFO we need to be a little smart about the order of these queues. 
we need a way to add the recent element to our list before adding the older element. 
One list can be temporary storage storing our recent element, if a new element is added and there is something in that queue,
then we simply add the recent element to the other queue, and then pop the now old element from the recenet queue and add that to our other queue as well.

I like this idea but it fails after 4 elements. One thing we can try is reversing the list as soon as a 3rd element is added. i.e
1, 2, 3, 4
list1: [1] -> []     -> [3]    -> [4, 3, 2, 1]
list2: []  -> [2, 1] -> [2, 1] -> []

basically we temporarly store the new element in one of the lists, and keep the stack in another. If we dont have a free list we pop the single element from the temp list
add our new element to the temp list, add the popped element back to the temp lis  and then pop / add everything from the stack list into the temp list and then switch the two.
Doing this preserves the order 

I think the intuition I have is right but I am trying to skip steps, I need to implement the inefficent version first. Add to list and pop everything from other list.
We swap the queues beacuse when a new element is added if its added to the exisitng main queue then due to fifo it wont be the next element in the pop. We need to add it
to the temp queue. Then we need to take all the elements from the first queue and add them to the temp queue in the correct order, now the temp queue has all the items 
of our stack which means it not acts as our main queue.
"""
class MyStack:

    def __init__(self):
        self.mainQueue = Queue()
        self.tempQueue = Queue()

    def push(self, x: int) -> None:
        # swap queues so that we preserve the mainQueue's order 
        temp = self.mainQueue
        self.mainQueue = self.tempQueue
        self.tempQueue = temp
        
        self.mainQueue.enqueue(x)
        element = self.tempQueue.dequeue()
        while element:
            self.mainQueue.enqueue(element)
            element = self.tempQueue.dequeue()
        

    def pop(self) -> int:
        return self.mainQueue.dequeue()
        

    def top(self) -> int:
        top = self.pop()
        if top:
            self.push(top)
        return top
        

    def empty(self) -> bool:
        return self.top() == None

"""
Another idea, alternate the add and push 
1, 2, 3, 4
list1: [1, 3]
list2: [2, 4]


No this dose not preserve order

"""

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()