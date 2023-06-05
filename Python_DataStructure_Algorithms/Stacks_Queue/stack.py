class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# FILO
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:   
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self): 
        if self.height ==0:
            return None
        temp = self.top
        self.top = self.top.next
        self.temp = None
        self.height -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(4)
my_stack.push(3)
print(my_stack.pop().value)
print(my_stack.pop().value)

print('Top:', my_stack.top)
print('Height:', my_stack.height)
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""
