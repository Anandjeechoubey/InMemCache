from .memory.memory import Memory
from .memory.standard import LRU
from threading import Lock
from typing import Hashable

class InMemCache:
    def __init__(self, memory = LRU(), max_size = None):

        assert isinstance(memory, Memory), f"memory must be of type {Memory}, {type(memory)} detected instead"
        assert isinstance(max_size, int) or max_size == None, f"max_size must be an integer, {type(max_size)} detected instead"

        self.__mem = memory
        self.__max_size = max_size
        self.__size = 0
        self.__lock = Lock()
    
    def __getitem__(self, key):

        assert isinstance(key, Hashable), f"{key}: {type(key)} is not hashable"

        try:
            with self.__lock:
                return self.__mem[key]
        except KeyError as k:
            return None

    def __setitem__(self, key, value):

        assert isinstance(key, Hashable), f"{key}: {type(key)} is not hashable"

        with self.__lock:
            if (self.__size == self.__max_size):
                self.__mem.evict()
                self.__size -= 1

            self.__mem[key] = value
            self.__size += 1

    def __len__(self):

        with self.__lock:
            return self.__size
        
    def __contains__(self, key):

        assert isinstance(key, Hashable), f"{key}: {type(key)} is not hashable"

        with self.__lock:
            return key in self.__mem