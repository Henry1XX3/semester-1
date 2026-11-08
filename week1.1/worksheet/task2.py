"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
value = input("Please enter the amount you want to save every month in £")

#try and change the value to an integer, if it cannot be changed into an integer or crashes the program
#then print "invalid amount" and quit the program
try:
    value = int(value)
except:
    print("Invalid amount")
    quit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
totalSaved = value * 12
print("By the end of the year you will have saved £" ,totalSaved )

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
totalWithInterest = totalSaved * 1.008
print(f"By the end of the year you will have saved £{totalWithInterest:.2f}")


