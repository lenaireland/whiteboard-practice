# 11.04.18

# Part I - What do the following lines of code give you?
A1 = range(10)

A2 = sorted([i for i in A1 if i in A1])

A3 = [i for i in A1 if i in [4, 5, 6]]

A4 = {i:i*i for i in A1}

A5 = [[i,i*i] for i in A1]

# Given the LRU_Cache class below (with self.size in __init__ and the skeleton of the methods
# get and put, complete __init__, along with get and put.)


class LRU_Cache():
    """Size-limited associative storage that will, when full, discard the least recently used key"""


    def __init__(self, maxsize=3):
        self.double_list = DoubleLinkedList()
        self.max_size = maxsize
        self.key_to_node = {}
        self.size = 0

    def get(self, key):
        """Retrieves the value associated with key returns None if the key is not present"""

        if key in self.key_to_node:
            node = self.key_to_node[key]
            ret_val = node.value

            if self.double_list.head.next != node:
                self.double_list.unlink_node(node)
                self.double_list.add_to_front(node)

            return ret_val


    def put(self, key, value):
        """Associates a value with a key.  If a new key is introduced,and would result in size being exceeded, remove the value least recently assigned or retrieved."""

        node = None

        if key not in self.key_to_node:
            # add it
            node = Node(key, value)
            self.key_to_node[key] = node
            self.size += 1
        else:
            node = self.key_to_node[key]
            node.value = value
            self.double_list.unlink_node(node)
            
        self.double_list.add_to_front(node)

        # Do we need to kick items out of LRU?
        if self.size > self.max_size:
            lru_node = self.double_list.tail.prev
            self.key_to_node.pop(lru_node.key)
            self.double_list.unlink_node(lru_node)
            self.size -= 1


Class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail
        self.head.prev = self.head

    def unlink_node (self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node


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
