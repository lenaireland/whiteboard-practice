# 11.04.18

# Part I - What do the following lines of code give you?
A1 = range(10)

A2 = sorted([i for i in A1 if i in A1])

A3 = [i for i in A1 if i in [4, 5, 6]]

A4 = {i:i*i for i in A1}

A5 = [[i,i*i] for i in A1]

# Given the LRU_Cache class below (with self.size in __init__ and the skeleton of the methods
# get and put, complete __init__, along with get and put.)


# Note: this would be better with a doubly-linked list
# (wouldn't have to re-index every time you move around items in cache - saves runtime)

class LRU_Cache():
    """Size-limited associative storage that will, when full, discard the least recently used key"""

    def __init__(self, size=3):
        self.size = size
        self.lru = []

    def get(self, key):
        """Retrieves the value associated with key returns None if the key is not present"""

        for item in self.lru:
            if item[0] == key:
                self.lru.remove(item)
                self.lru.append(item)
                return item[1]

        return None


    def put(self, key, value):
        """Associates a value with a key.  If a new key is introduced,and would result in size being exceeded, remove the value least recently assigned or retrieved."""

        for item in self.lru:
            if item[0] == key:
                self.lru.remove(item)
                self.lru.append((key, value))
                return

        if len(self.lru) < self.size:
            self.lru.append((key,value))
        elif len(self.lru) >= self.size:
            self.lru.pop(0)
            self.lru.append((key,value))





def unit_test():
    test_cache = LRU_Cache(2)

    test_cache.put(1, "alpha")

    test_cache.put(2, "beta")

    test_cache.put(3, "charlie")

    test_cache.put(4, "delta")

    print(test_cache.get(1))
    print(test_cache.get(4))

    test_cache.put(2, "epsilon")

    test_cache.put(5, "foxtrot")

    print(test_cache.get(2))


if __name__ == "__main__":
    unit_test()
