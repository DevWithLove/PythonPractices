
# int: 1, 3 ,5 / str: use '' or " " / bool : True or False / float o.3212

# x = 5 
# x = "test"
# x = True
# X = False  #captial is matter , different variable as x
# print(x, X)

## convert string to int
# x = "5"
# y = "6"
# print(x +y) # =>56
# print(int(x) + int(y)) #=> 11
# print(type(x))

# if 5 < 6: 
#     print(True)
# else:
#     print(False)

# and, or not()
# x = 2
# y = 3 
# if not(y == 3 and x != 2): 
#     print('Yes')

# for x in range(0, 10, 1): # start, stop , step
#     print(x)
# for x in range(10, 0, -1):
#     print(x)

# x = 0
# while x <= 10: 
#     print(x)
#     if x==5: break
#     x+=1

# fruits = ['apple', 5, 3.4, True]
# print(fruits)
# for n in fruits: 
#     print(n)

# fruits.append("pear")
# fruits[1] = "Blueberry"

# for index, value in enumerate(fruits): 
#     print(value, 'at index: ', index)

# for i in range(len(fruits)):
#     print(fruits[i])

# position = (2, 3)
# print(type(position), position[1])

###### String methods
# x = "   Test 2     ddd"
# print(x)
# print(x.strip()) # remove space before an after
# print(len(x))
# print(x.lower())
# print(x.upper())
# print(x.split( ))

####### slice operater  str[start:stop:step]
# x = "Hello I like python"
# print(x[1])
# print(x[0:6]) 
# print(x[6:])  # From 6 to end
# print(x[::2]) # default begin to end, step 2

# x = ["a", "b", "c", "d"]
# print(x[1:])
# #x[0:0] = "1" # insert begining
# x[1:1] = "2" # insert at 1
# print(x)

# def addTwo(x): 
#     return x+2

# print(addTwo(5))

# .find(), .count()
# s = 'hello'
# print(s.find('l')) # give me the first index of the l
# print(s.find('h'))
# print(s.find('t')) # return -1 not find any

# print(s.count('l')) # number of 'l'
# print(s.count('t')) # number of 't'

#### optionnal paramaters
# def func(x, test='2'): 
#     print(x, test)
# func("t1")

# class number(): 
#     def __init__(self, num):
#         self.var = num

#     def display(self):
#         print(self.var)

# n = number(32)
# n.display()
# print(n)

# x = [i for i in range(10) if i % 2 ==0]
# print(x)

# def func(*args):
#     print(args)
# func(1,2,3,4,5,"test")

######### Alphabet soup #####

# def alphabetOrder(str):
#     lookup = "abcdefghijklmnopqrstuvwxyz"
#     sorted = ""
#     for l in lookup:
#         count = str.count(l.upper())
#         if count > 0 :
#             sorted = sorted + (l.upper()*count)
#         count = str.count(l)
#         if count > 0:
#             sorted = sorted + (l*count)
    
#     return sorted

# def alphabetOrder2(str):
#     # remove duplciated char in lower case
#     chars = "".join(set(str.lower()))
#     # get a sorted look up
#     lookupInOrder = "".join(sorted(chars))

#     newStr = ""
#     for l in lookupInOrder:
#         count = str.count(l.upper())
#         if count > 0 :
#             newStr = newStr + (l.upper()*count)
#         count = str.count(l)
#         if count > 0:
#             newStr = newStr + (l*count)

#     return newStr

# print(alphabetOrder2("hello"))
# print(alphabetOrder2("eLEPhAnt"))

#### Magic Squares ######
# https://www.youtube.com/watch?v=-qs7QocYUbQ&list=PLzMcBGfZo4-l73euhrUu0exrXc_1HQPV0&index=2

# def isMagicSquares(numberOfRow, *args): 
#     if numberOfRow != len(args) or numberOfRow == 0: 
#         return False

#     target = sum(args[0])
#     # check rows
#     for row in args:
#         if sum(row) != target: 
#             return False
    
#     # check cols
#     for col in range(numberOfRow):
#         col_sum = 0
#         for row in range(numberOfRow):
#             col_sum += args[row][col]
#         if col_sum != target: 
#             return False
    
#     # check main diagonal
#     diag_sum = 0
#     for i in range(numberOfRow):
#         diag_sum += args[i][i]
#     if diag_sum != target: 
#         return False
    
#     # check secondary diagnora
#     diag_sum2 = 0
#     for i in range(numberOfRow-1,-1,-1):
#         diag_sum2 += args[i][i]

#     if diag_sum2 != target:
#         return False
    
#     return True

# print(isMagicSquares(3, [2,7,6],[9,5,1],[4,3,8]))
# print(isMagicSquares(4, [16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]))

###### String Compression #############
# https://www.youtube.com/watch?v=mWU7t6Wu9sM&list=PLzMcBGfZo4-l73euhrUu0exrXc_1HQPV0&index=5

# def stringCompression(str):
#     newStr = ""
#     sub = str[0]
#     for c in str[1:]:
#       if sub.find(c) != -1 :
#          sub += c
#       else:
#         newStr += f"{len(sub)}{sub[0]}"
#         sub = c
    
#     newStr += f"{len(sub)}{sub[0]}"
#     return newStr

# print(stringCompression("+++=====!!!!!!!"))


# test = [1,2,3,4,5]
# testR = test[::-1] #revers 
# print(test)
# print(testR)
