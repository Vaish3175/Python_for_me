# To take inout from user use input()

age = input("Enter your age\n")       # Here input is taken as a string

age = int(age)           # Converting string input to integer input

if(age>18):                               # If age is greater than 18 it will print you can drive a car
    print("You can drive a car")          # If age is less than 18 it will print else statement

elif(age==18):                            # If age is equal to 18 it will print you are an awesome teen
    print("You are an awesome teen")      # If age is not equal to 18 it will print the else statement

else:
    print("You cannot drive a car")

# LOOPS
# To print numbers between 1 to 1000
for i in range(0, 1000):
    print(i)

# Loops (iterative Statements)
li = [1,432,"that"]
for item in li:
    print(item)



# WHILE LOOP
i = 0
while(i<10):
    i = i+1
    print(i)

# Break and Continue
i = 0
while(i<10):
    i = i+1
    if i == 7:            # It breaks the flow when i becomes 7 skips 8 and continues for 9
        continue
    print(i+1)