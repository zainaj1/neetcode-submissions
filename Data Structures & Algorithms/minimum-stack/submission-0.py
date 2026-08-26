class MinStack:
    def __init__(self):
        self.stack = []
    
    # [1, 1, 2]
    def push(self, val: int) -> None:
        minVal = val if val < self.getMin() else self.getMin()
        self.stack.append(val)
        self.stack.append(minVal)        
        
    def pop(self) -> None:
        self.stack.pop() # Remove the min val associated with it
        self.stack.pop() # Remove the currnt val
        

    def top(self) -> int:
        return self.stack[-2] # -2 because the second last index is min val
        

    def getMin(self) -> int:
        if (self.stack):
            return self.stack[-1] 
        return float('inf')

