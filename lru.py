# whiteboarding with Sue and Tien

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def unlink(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def add_to_front(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_last_node(self):
        last = self.tail.prev
        self.unlink(last)
        del(last)


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_to_node = {}
        self.double_list = DoubleLinkedList()
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_to_node:
            node = self.key_to_node[key]
            # move to most recently used position
            self.double_list.unlink(node)
            self.double_list.add_to_front(node)
            return node.value
        # key wasn't in the cache
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key_to_node:
            # already in there, so just update the value
            node = self.key_to_node[key]
            node.value = value
            # remove it from its position in lRU cache, so in next step can
            # move it to the most-recently-used position
            self.double_list.unlink(node)
        else:
            # item wasn't already in LRU cache, so add it.
            node = Node(key, value)
            self.key_to_node[key] = node
            self.size += 1
        # place node in most-recently-used position, at front of double_list
        self.double_list.add_to_front(node)

        if self.size > self.capacity:
            # need to evict least recently used
            lru_node = self.double_list.tail.prev
            del(self.key_to_node[lru_node.key])
            self.double_list.remove_last_node()
            self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)