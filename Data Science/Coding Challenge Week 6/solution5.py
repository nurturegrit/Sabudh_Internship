class Node:
    def __init__(self, key: int = None, value: int = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hashmap to store the key-node pairs
        # Dummy head and tail nodes to simplify edge case handling
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Removes a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        """Adds a node right after the head."""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front (most recently used)
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value of the existing node and move it to the front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)
            
            # If the cache exceeds capacity, remove the least recently used node
            if len(self.cache) > self.capacity:
                # Least recently used node is just before the tail
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
