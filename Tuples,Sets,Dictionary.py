'''Python Collections:
    1. List
    2. Tuple
    3. Set
    4. Dictionary
'''

# Tuples
''' Items in a list can be changed but items in a tuple cannot '''
''' List have [] but tuples have () '''

a = ("Harry", "Shub", "Rohan")
print(a)
var = type(a)
print(var)
# a[0] = "Vikrant"     We cannot change any element in a tuple

# Typecasting can be done i.e. convert tuple to list and the add or replace elements
for item in a:
    print(item)


# Set
# removes all duplicate elements
s1 = {1,2,3,4,5,23,63,53,54,85,2,22,23,45,6}
print(s1)
# adding a single number
s1.add(4444)
print(s1)
# updating a set
s1.update([162,115,699,120,])
print(s1)
# length of the set
print(len(s1))
# remove a element
   #if element is present in the set it removes it or else it throws an error
s1.remove(4444)
print(s1)
# s1.remove(5555) will give us error because 5555 is not present in the set s1
# To avoid error use discard method
s1.discard(5555)
print(s1)

for item in s1:
    print(s1)

'''Other methods
    .pop
    .clear
    del
    and
    intersection
    union
    etc....'''

# Dictionary is a key-value pair.

VaishDict = {"Name":"Vaishu", "Class": "4th", "Marks":"96", "Hours in school":6}
print(VaishDict)
# Finding a particular value
print(VaishDict["Marks"])
# Updating a value
VaishDict["Marks"] = 98
print(VaishDict["Marks"])

for item3 in VaishDict:
    print(item3)

''' Search new method for dictionary on the net. '''