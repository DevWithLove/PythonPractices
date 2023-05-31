
# Unlimited Arguments
def add(*args):
    # it is tuple
    print(type(args))
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(1, 2, 3, 4, 56, 78, 10))

# Many Keyword arguments
def calculate(n, **kwargs):
    # it is dict
    print(type(kwargs))
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add=3, multiply=5))

class Car:
    def __init__(self, **kw):
        # if user not provide the key , we will get error
        self.make = kw["make"]
        # use get, if user not provide the key, it will return None instead of an error
        self.model = kw.get("model")

myCar = Car(make = "Nissan", model="GT-R")
print(myCar.model)
