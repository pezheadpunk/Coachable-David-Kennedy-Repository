'''146. LRU Cache'''
from collections import deque

class LRUCache:
    '''
    When creating the oject stores the capacity and creates a dictionary to
    serve as the cache to retrive key, objects in O(1) time, and a deque to
    keep track of the keys as they are used. Has the get function to get to
    retrieve the value of the given key while updating the LRU deque. Also 
    has the put fucntion that adds a key, value to the cache or updates it
    if it already exists in the cache while aslo updating/ adding the key 
    the to the LRU deque and if the capacity is reached, removing the least
    recently used key, value from the deque and the cache
    Runtime: O(n) -> removing values from the deque
    Space O(n) -> where n is the capacity for the cache dictionary and     
                  deque
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = deque()    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            if len(self.lru) + 1 > self.capacity:
                del_key = self.lru.popleft()
                del self.cache[del_key]
            self.lru.append(key)
        self.cache[key] = value