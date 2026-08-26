class Heap:
    def __init__(self):
        self.elements = [0]
    
    def peak(self) -> int:
        return self.elements[1]
    
    def size(self) -> int:
        return len(self.elements) - 1
    
    def insert(self, val):
        self.elements.append(val)
        i = len(self.elements) - 1
        while i > 1 and self.elements[i] < self.elements[i//2]:
            self._swap(i//2, i)
            i = i//2

        print(self.elements)

    def pop(self):
        if len(self.elements) == 1:
            return None
        if len(self.elements) == 2:
            return self.elements.pop()
        
        res = self.elements[1] 
        self.elements[1] = self.elements.pop()
        i = 1
        while i * 2 < len(self.elements):
            if (2 * i + 1 < len(self.elements) and 
            self.elements[2 * i + 1] < self.elements[2 * i] and 
            self.elements[2 * i + 1] < self.elements[i]):

                self._swap(2 * i + 1, i)
                i = 2 * i + 1
            elif self.elements[2 * i] < self.elements[i]:
                self._swap(2 * i, i)
                i = 2 * i
            else:
                break
        
        return res
    
    def _swap(self, start, end):
        temp = self.elements[start]
        self.elements[start] = self.elements[end]
        self.elements[end] = temp
    
    def _has_right_child(self, index):
        return 


class KthLargest:
    k = 0
    heap = None
    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        self.k = k
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        if self.heap.size() < self.k:
            self.heap.insert(val)
        elif self.heap.peak() < val:
            self.heap.insert(val)
            self.heap.pop()
        return self.heap.peak()

       
            


        








