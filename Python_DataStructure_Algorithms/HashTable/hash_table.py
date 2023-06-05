

class HashTable:
    def __init__(self, size = 7):
        # create list with 7 items and all items are none
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # ord: get the ASCII number for each letter
            # 23 is prime number, we can use any prime number in here
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None: 
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key): 
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        keys = []
        for item in self.data_map:
            if item != None:
                for i in range(len(item)):
                    if item[i][0] is not None:
                        keys.append(item[i][0])
        return keys
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

# interview question, find if there is common item between 2 lists
def item_in_common(list1, list2):
    table = {}
    for i in list1:
        table[i] = True
    for j in list2:
        if j in table:
            return True
    return False


list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))



hash_table = HashTable()
hash_table.set_item('bolts', 1400)
hash_table.set_item('washers', 50)
hash_table.set_item('lumber', 70)

print(hash_table.get_item('bolts'))
print(hash_table.get_item('washers'))
print(hash_table.get_item('lumber'))

print(hash_table.keys())

#hash_table.print_table()
