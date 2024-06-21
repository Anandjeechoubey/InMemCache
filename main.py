# Example Usage - LRU
from cache import InMemCache

def main():

    eviction_policies = ['LRU', 'FIFO', 'LIFO', 'LFU']

    for policy in eviction_policies:
        print(f"Example of: {policy} policy -- ")
        cache = InMemCache(max_size=3, eviction_policy=policy)
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")

        print(cache.get("key1"))  # Output: value1
        cache.set("key4", "value4")  # This will evict the least recently used item (key2 if LRU policy is chosen)
        print(cache.get("key2"))  # Output: None (evicted if LRU policy is chosen)
        cache.set("key5", "value5")  # Eviction happens based on the chosen policy
        print(cache.get("key3"))  # Output depends on eviction policy


if __name__ == "__main__":
    main()