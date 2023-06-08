"""
Sets are similar to dictionaries except that instead of having key/value pairs they only have the keys but not the values.

Like dictionaries, they are implemented using a hash table (which is why we are covering them here).

Sets can only contain unique elements (meaning that duplicates are not allowed). 

They are useful for various operations such as finding the distinct elements in a collection and performing set operations such as union and intersection.

They are defined by either using curly braces {} or the built-in set() function like this:



"""

# # Create a set using {}
# my_set = {1, 2, 3, 4, 5}
 
# Create a set using set()
my_set = set([1, 2, 3, 4, 5])

# Add an element to a set
# If the number 6 is already in the set it will not be added again.
my_set.add(6)
print(f"after add 6 {my_set}")
 
# Update is used to add multiple elements to the set at once. 
# It takes an iterable object (e.g., list, tuple, set) as an 
# argument and adds all its elements to the set. 
# If any of the elements already exist in the set, 
# they are not added again.
my_set.update([3, 4, 5, 6])
print(f"after updated elements {my_set}")
 
# Removing an element from a set
my_set.remove(3)
print(f"after remove 3 {my_set}")
 
# Union of two sets
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
print(f"union two sets {union_set}")
 
# Intersection of two sets
intersection_set = my_set.intersection(other_set)
print(f"intersection_set {intersection_set}")
 
# Difference between two sets
difference_set = my_set.difference(other_set)
print(f"difference_set {difference_set}")
 
# Checking if an element is in a set
if "hello" in my_set:
    print("Found hello in my_set")




