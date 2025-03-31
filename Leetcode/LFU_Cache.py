from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}  # {key: (value, freq)}
        self.freq_to_keys = defaultdict(OrderedDict)  # {freq: OrderedDict(keys)}
        self.min_freq = 0  

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1  
        
        value, freq = self.key_to_val_freq[key]
        self._update_freq(key, value, freq)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.key_to_val_freq:
            _, freq = self.key_to_val_freq[key]
            self._update_freq(key, value, freq)
        else:
            if len(self.key_to_val_freq) >= self.capacity:
                self._evict_lfu()
            
            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_keys[1][key] = None 
            self.min_freq = 1  

    def _update_freq(self, key: int, value: int, freq: int):

        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:  
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1  

    
        new_freq = freq + 1
        self.key_to_val_freq[key] = (value, new_freq)
        self.freq_to_keys[new_freq][key] = None  # Maintain LRU order

    def _evict_lfu(self):

        key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)  # Remove first (least recently used)
        del self.key_to_val_freq[key]  # Remove from cache
        
        if not self.freq_to_keys[self.min_freq]:  # If frequency list is empty
            del self.freq_to_keys[self.min_freq]

# Testing the LFU Cache with Example Case
lfu = LFUCache(2)

lfu.put(1, 1)  # cache=[1,_], cnt(1)=1
lfu.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lfu.get(1))  # return 1, cache=[1,2], cnt(1)=2, cnt(2)=1
lfu.put(3, 3)  # Evicts key 2 (LFU), cache=[3,1], cnt(3)=1, cnt(1)=2
print(lfu.get(2))  # return -1 (not found)
print(lfu.get(3))  # return 3, cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)  # Evicts key 1 (LRU tie), cache=[4,3], cnt(4)=1, cnt(3)=2
print(lfu.get(1))  # return -1 (not found)
print(lfu.get(3))  # return 3, cache=[3,4], cnt(3)=3, cnt(4)=1
print(lfu.get(4))  # return 4, cache=[4,3], cnt(3)=3, cnt(4)=2
