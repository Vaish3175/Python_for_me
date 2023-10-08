# Python is a object oriented programming language

# Class and Objects are used so that we do not have to repeat things again and again.

'''Class
    A class is like a template. 
    
    Made by using many variables and functions.

    One class can have many objects.'''

class DemoClass:            # colon starts a class
    # Making variable in class
    a = 10

    # Making function in class
    ''' Method and Functions are somewhat same.
    But a Method can be defined only inside a class but function can be defined outside or inside a class.'''
    def sumvalue(self):
        print(20+30)
    
# Making object in a class
# By using ()
demoObject = DemoClass()
# Calling a variable in a class
print(demoObject.a)

# Calling a function in a class
demoObject.sumvalue()


