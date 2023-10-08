'''Python Collections:
    1. List
    2. Tuple
    3. Set
    4. Dictionary
'''

# List
lst = [61,2,3,4,5,6,41]
print(lst)
var = type(lst)
print(var)

# Slicing a list
var = lst[3]
print(var)
# Changing element in a list
lst[2] = 45
print(lst)
# append method
lst.append(100)
print(lst)
# insert method
lst.insert(1,100)       # inserts 100 in place of 1
print(lst)
# remove method
lst.remove(61)
print(lst)
# pop method
lst.pop()        # removes last element of the list
print(lst)
# del method       # to remove any element with index number
del lst[1]           # removes element on index 1
print(lst)           

lst.clear()     # clears the list
print(lst)

del lst        # deletes the whole list

# for more methods search list methods in python on net.
