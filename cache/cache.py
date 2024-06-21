import time
import collections

class CacheEntry:
    def __init__(self, value):
        self.value = value
        self.timestamp = time.time()
        self.frequency = 0

class InMemCache:
    def __init__(self, max_size=100, eviction_policy='LRU'):
        self.max_size = max_size
        self.eviction_policy = eviction_policy
        self.cache = {}
        self.order = collections.OrderedDict()  # Used for LRU and FIFO
        self.stack = []  # Used for LIFO
        self.freq_map = collections.defaultdict(int)  # Used for LFU

    def _evict_if_necessary(self):
        if len(self.cache) >= self.max_size:
            if self.eviction_policy == 'LRU':
                oldest = self.order.popitem(last=False)
                del self.cache[oldest[0]]
            elif self.eviction_policy == 'FIFO':
                oldest = next(iter(self.order))
                del self.order[oldest]
                del self.cache[oldest]
            elif self.eviction_policy == 'LIFO':
                newest = self.stack.pop()
                del self.cache[newest]
            elif self.eviction_policy == 'LFU':
                least_freq = min(self.freq_map.values())
                least_freq_keys = [k for k, v in self.freq_map.items() if v == least_freq]
                key_to_evict = least_freq_keys[0]
                del self.cache[key_to_evict]
                del self.freq_map[key_to_evict]

    def set(self, key, value):
        self._evict_if_necessary()
        entry = CacheEntry(value)
        self.cache[key] = entry
        
        if self.eviction_policy in ['LRU', 'FIFO']:
            self.order[key] = entry.timestamp
            if self.eviction_policy == 'LRU':
                self.order.move_to_end(key)
        elif self.eviction_policy == 'LIFO':
            self.stack.append(key)
        elif self.eviction_policy == 'LFU':
            self.freq_map[key] += 1

    def get(self, key):
        if key not in self.cache:
            return None
        entry = self.cache[key]
        entry.timestamp = time.time()
        
        if self.eviction_policy == 'LRU':
            self.order.move_to_end(key)
        elif self.eviction_policy == 'LFU':
            self.freq_map[key] += 1
        
        return entry.value

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            if self.eviction_policy in ['LRU', 'FIFO']:
                del self.order[key]
            elif self.eviction_policy == 'LIFO':
                self.stack.remove(key)
            elif self.eviction_policy == 'LFU':
                del self.freq_map[key]

    def clear(self):
        self.cache.clear()
        self.order.clear()
        self.stack.clear()
        self.freq_map.clear()


