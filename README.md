# InMemCache

InMemCache is a Python library for in-memory caching with support for multiple eviction policies such as LRU, FIFO, LIFO, and LFU.

## Installation

pip install -i https://test.pypi.org/simple/ InMemCache

## Usage

```python
from cache import InMemCache

cache = InMemCache(max_size=3, eviction_policy='LRU')
cache.set("key1", "value1")
cache.set("key2", "value2")
cache.set("key3", "value3")

print(cache.get("key1"))  # Output: value1
cache.set("key4", "value4")  # This will evict the least recently used item
print(cache.get("key2"))  # Output: None (evicted)
```
