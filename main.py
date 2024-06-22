# Example Usage - LRU
from cache.cache import InMemCache
from cache.memory.standard import FIFO, LIFO, LRU

def main():

    print("Example of FIFO eviction in mem cache")
    cache = InMemCache(memory = FIFO(), max_size = 3)

    for i in range(5):
        cache.__setitem__(f"key{i}",f"value{i}")

    for i in range(5):
        print(cache.__getitem__(f"key{i}"))

    print("Example of LIFO eviction in mem cache")
    cache = InMemCache(memory = LIFO(), max_size = 3)

    for i in range(5):
        cache.__setitem__(f"key{i}",f"value{i}")

    for i in range(5):
        print(cache.__getitem__(f"key{i}"))

    print("Example of LRU eviction in mem cache")
    cache = InMemCache(memory = LRU(), max_size = 3)

    for i in range(5):
        cache.__setitem__(f"key{i}",f"value{i}")

    for i in range(5):
        print(cache.__getitem__(f"key{i}"))


if __name__ == "__main__":
    main()