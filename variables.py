# Variables are like containers

a = 34          # interger datatype
b = "Harry"      # string datatype
c = 45.32       # float datatype

print(a+33)

''' Rules for variables
    1. Variables should with a letter or an underscore
    2. Variables cannot start with a number
    3. It can only contain alpha numberic characters
        i.e use only a,b,c,d,e,f......
            cannot use c*,d*.......
    4. Variable names are case sensitive
        i.e. harry and Harry are two different variables'''

# Finding type of a variable
typeA = type(a)
typeB = type(b)

print(typeB)

e = 31
print(type(e))

# TypeCasting
f = "31"         # here f is a string

# print(f+2) will give us a error because we cannot add integer to a string

f = int(f)      # converts string f into integer f
print(f+2)

f = float(f) 
print(f+2)