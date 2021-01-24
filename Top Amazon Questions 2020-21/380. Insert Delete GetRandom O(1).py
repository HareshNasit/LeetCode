class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elems_dict = {}
        self.elems_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.elems_dict:
            self.elems_dict[val] = len(self.elems_list)
            self.elems_list.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.elems_dict:
            last_elem = self.elems_list[-1]
            val_index = self.elems_dict[val]
            self.elems_list[val_index], self.elems_dict[last_elem] = last_elem, val_index
            self.elems_list.pop()
            del self.elems_dict[val]
            return True
        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # rand_num = random.randint(0, len(self.elems_dict) - 1)
        return choice(self.elems_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
