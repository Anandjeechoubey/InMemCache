# InMemCache

InMemCache is a thread safe Python library for in-memory caching with support for multiple eviction policies such as LRU, FIFO, LIFO, and LFU.

## Installation

pip install -i https://test.pypi.org/simple/ InMemCache

### Run Unit Tests

```
make test
```

### Use the library

To use the cache functionality,

```python
from cache.cache import InMemCache

# the default eviction policy is LRU
cache = InMemCache()
```

To use standard eviction policies

```python
from cache.cache import InMemCache
from cache.memory.standard import FIFO, LIFO

cache = InMemCache(memory = FIFO(), capacity = 100)
```

To define custom eviction policies

```python
from cache.cache import InMemCache
from cache.memory.memory import Memory

class CustomMemory(Memory):
    # implement all the required methods here
    pass

cache = InMemCache(memory = CustomMemory(), capacity = 100)
```
