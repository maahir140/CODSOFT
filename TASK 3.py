#                TASK :- 03
#                RANDOM PASSWORD GENERATOR  depends upon the user specified length 

#  import random module that generating random numbers
import random

# import string module for the access of all constant
import string

# add the all string imported letters, numbers and symbols in one variable
list1 = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

# prompt the user to specify the length of the password that is want to generate
len = int(input("Enter the lenght of the password that you want: "))

password = "" # empty string in which the generated letters are added

# using loop for the genration of random password
for i in range(len):
    password += random.choice(list1) #generated letters are added in the paaword empty string

# display the generated password
print("Your Random Genrated Password:", password)
