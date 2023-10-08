# Triple quotes can be comment but if written in a variable they are a string

name = '''I am happy'''
print(name)

'''Indexing starts with zero in many programming language.
   PYTHON is one of those programming languages.'''

# Slicing a string
sname = "Vaishnavi"
print(sname[0])       # it will give me the zeroth character of the string sname

print(sname[1])
print(sname[4])
print(sname[5])
# print(sname[10])      # 10 is out of range so it will give us a error

print(sname[2:5])      # characters as output will be 2nd, 3rd, 4th
                       # 5th will not be the output  range is [ a : b] output is a,...,b-1

print(sname)

# strip function removes all the extra spaces
print(name.strip()) 

# gives us the length of the string
print(len(sname))       

# converts string to lower case
var = sname.lower()     

# converting string to UPPERCASE
var = sname.upper()    

# for replacing a element
var = sname.replace("i","t")
print(var)

# other use of replace function
student = "harry, Shubham, aradhya, Heena"
        # replacing ',' with blank
study = student.replace(","," ")
print(study)
        # to bring every name on new line
study = student.replace(", ","\n")
print(study)

# Concatination of strings
stri = "This is a"
stri1 = "This is not a"
print(stri + stri1)

# .format syntax
name1 = "Rohan"
name2 = "Harry"

# temp = "This is a boy named {} and he is a boy named {}".format(name1,name2)
# print(temp)

# by default here name1 has index 0 and name2 has index 1
temp1 = "This is a boy named {0} and he is a boy named {1}".format(name1,name2)
print(temp1)
# by replacing these index numbers
temp2 = "This is a boy named {1} and he is a boy named {0}".format(name1,name2)
print(temp2)

# alternative for .format is f string
temp3 = f"This is a boy named {name1} and he is a boy named {name2}"
print(temp3)

''' OPERATORS:
              '+' is ADDITION
              '-' is SUBTRACTION
              '*' is MULTIPLICATION
              '/' is DIVISION
              '**' is EXPONENTIATION OPERATOR
              '//' is FLOOR DIVISION OPERATOR
              '%' is MODULO OPERATOR'''
a = 12
b = 6
print("Addition is",a+b)
print("Subtraction is",a-b)
print("Multiplication is",a*b)
print("Division is",a/b)
print("Exponential is",a**b)
print("Floor division is",a//b)
print("Modulo is", a%b)
   
