class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.leastRecentlyUsed = None
        self.mostRecentlyUsed = None
        self.capacity = capacity 
        self.cache = {}
    
    def _remove(self, node):
        if node.next and node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.next:
            self.leastRecentlyUsed = node.next
            node.next.prev = None
        elif node.prev:
            self.mostRecentlyUsed = node.prev
            node.prev.next = None
        else:
            self.mostRecentlyUsed = None
            self.leastRecentlyUsed = None
        
        # Might not need but good for cleanup      
        node.next = None
        node.prev = None
    
    def _insert(self, node):
        if not self.leastRecentlyUsed and not self.mostRecentlyUsed:
            self.leastRecentlyUsed = node
            self.mostRecentlyUsed = node
        elif not self.mostRecentlyUsed:
            self.mostRecentlyUsed = node
            node.prev = self.leastRecentlyUsed
            self.leastRecentlyUsed.next = node
        else:
            self.mostRecentlyUsed.next = node 
            node.prev = self.mostRecentlyUsed
            self.mostRecentlyUsed = node 
        

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        
        self._remove(node)
        self._insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        node = self.cache.pop(key, None)
        if node:
            self._remove(node)
        
        node = Node(key, value)
        self._insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove LRU node
            nodeToRemove = self.cache.pop(self.leastRecentlyUsed.key, None)

            if nodeToRemove:
                self._remove(nodeToRemove)
               

        

        
