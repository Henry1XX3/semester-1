# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

#prints the string the user entered without modifying it
print(f"\nOriginal String: {user_string}")
#makes every character in the string lower case
print(f"Modified String 1: {user_string.lower()}")
#makes every character in the string upper case
print(f"Modified String 2: {user_string.upper()}")
#returns a copy of the string with leading and trailing whitespace remove
print(f"Modified String 3: {user_string.strip()}")
#replaces any characters "a" with "@"
print(f"Modified String 4: {user_string.replace('a', '@')}")
#capitalise the first letter of the string
print(f"Modified String 5: {user_string.capitalize()}")
#prints the string in backward
print(f"Modified String 6: {user_string[::-1]}")
#return a version of the string where the first letter of each word is capitalised
print(f"Modified String 7: {user_string.title()}")
#returns the lenght of the string
print(f"Modified String 8: {len(user_string)}")
#returns the index where the character "a" is within the string
print(f"Modified String 9: {user_string.find('a')}")
#returns the number of times the letter "a" appears
print(f"Modified String 10: {user_string.count('a')}")
#returns a true or false value depending on wether or not the string starts with "Hello"
print(f"Modified String 11: {user_string.startswith('Hello')}")
#returns a true or false value depeninding on wether or not the string ends with "!"
print(f"Modified String 12: {user_string.endswith('!')}")
#Return true if the string is an alphabetic string, False otherwise.
print(f"Modified String 13: {user_string.isalnum()}")
#Return True if the string is an alphabetic string, False otherwise
print(f"Modified String 14: {user_string.isalpha()}")
#Return True if the string is a digit string, False otherwise.
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!
