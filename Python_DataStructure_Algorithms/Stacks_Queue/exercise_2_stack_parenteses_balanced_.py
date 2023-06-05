"""
Stack: Parentheses Balanced ( ** Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.
"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
    
def is_balanced_parentheses(parentheses):
    stack = Stack()
    for char in parentheses:
        if char == '(':
            stack.push(char)
        elif char == ')': 
           if stack.is_empty() or stack.pop() != '(':
               return False
     # If the stack is empty, the parentheses are balanced
    return stack.is_empty()



# def is_balanced_parentheses(text):
#     char_list =  list(text)
#     length = len(char_list)
#     if length % 2 != 0:
#         return False
#     first_half = char_list[0 : int(length/2)]
#     second_half = char_list[int(length/2) : length]
#     for index, item in enumerate(first_half):
#         if item == second_half[index]:
#             return False
#     return True




balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

print( is_balanced_parentheses(balanced_parentheses) )

print( is_balanced_parentheses(unbalanced_parentheses) )



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""