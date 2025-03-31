class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev  = None
        self.next = None
class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}

        #Dummy Node
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self,key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1
    
    def put(self,key,value):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        if len(self.cache) == self.capacity:
            self._remove(self.tail.prev)
        self._insert(Node(key,value))

    def _remove(self,node):
        del self.cache[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev 
    
    def _insert(self,node):
        self.cache[node.key] = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
# Test case
lRUCache = LRUCache(2)

lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
print(lRUCache.get(1))  # return 1

lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))  # return -1 (not found)

lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))  # return -1 (not found)
print(lRUCache.get(3))  # return 3
print(lRUCache.get(4))  # return 4