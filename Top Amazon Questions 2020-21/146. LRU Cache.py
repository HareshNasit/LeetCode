class LRUCache:
    # Logic: Use an OrderedDict for O(1) access and a list for getting the random
    # element
    capacity = 0
    elements = {}
    curr_size = 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elements = OrderedDict()
        self.curr_size = 0

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1
        self.elements.move_to_end(key)
        return self.elements[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.elements and self.curr_size + 1 <= self.capacity:
            self.elements[key] = value
            self.curr_size += 1
        elif key in self.elements:
            self.elements[key] = value
        else:
            self.elements.popitem(last=False)
            self.elements[key] = value
        self.elements.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
