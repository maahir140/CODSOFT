#                 TASK :- 02
#                 Simple Calcultor that help you in the calculation

# take a 1st no input from user
num1 = float(input('Enter the First no. '))
# take a 2nd no input from user
num2 = float(input('Enter the Second no. '))

# function for clculation
def add( x , y):
    # its a addtion function
    return(x+y)

def sub(x, y):
    # its a substration function
    return(x-y)

def mul(x, y):
    # its a multiply function 
    return(x*y)

def div(x, y):
    # its a divide function
    if y == 0:
        return "Error! Cannot divide by zero."
    return(x/y)

# Operator choice
print("Enter operator choice")
print("1 for addtion")
print("2 for substration")
print("3 for multiplication")
print("4 for divide")
choice = int(input(":- "))

# if elif condition for calculation
if choice == 1:
    print("Result: ", add(num1, num2)) # display the addition result
elif choice == 2:
    print("Result: ", sub(num1, num2)) # display the substraction result
elif choice == 3:
    print("Result: ", mul(num1, num2)) # display the multiplication result 
elif choice == 4:
    print("Result: ", div(num1, num2)) # display the divsion result

# Function ended here
print("Function Ended!")#                 TASK :- 02
#                 Simple Calcultor that help you in the calculation

# take a 1st no input from user
num1 = float(input('Enter the First no. '))
# take a 2nd no input from user
num2 = float(input('Enter the Second no. '))

# function for clculation
def add( x , y):
    # its a addtion function
    return(x+y)

def sub(x, y):
    # its a substration function
    return(x-y)

def mul(x, y):
    # its a multiply function 
    return(x*y)

def div(x, y):
    # its a divide function
    if y == 0:
        return "Error! Cannot divide by zero."
    return(x/y)

# Operator choice
print("Enter operator choice")
print("1 for addtion")
print("2 for substration")
print("3 for multiplication")
print("4 for divide")
choice = int(input(":- "))

# if elif condition for calculation
if choice == 1:
    print("Result: ", add(num1, num2)) # display the addition result
elif choice == 2:
    print("Result: ", sub(num1, num2)) # display the substraction result
elif choice == 3:
    print("Result: ", mul(num1, num2)) # display the multiplication result 
elif choice == 4:
    print("Result: ", div(num1, num2)) # display the divsion result

# Function ended here
print("Function Ended!")                



