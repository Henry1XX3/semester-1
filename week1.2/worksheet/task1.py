# Worksheet 1.2: Task 1 Solution
import sys

#input their number
gradeNum = input("Enter your grade (0-100): ")

#try and convert the input to an integer and check if it is within the valid range
try:
    gradeNum = int(gradeNum)
    if 0 <= gradeNum < 40:
        print(f"{gradeNum} is a Fail")
    elif 0 <= gradeNum < 70:
        print(f"{gradeNum} is a Pass")
    #if the grade is not within the valid range, exit the program with an error message
    elif 0 > gradeNum or gradeNum > 100:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    else:
        print(f"{gradeNum} is a Distinction")
#if it can't be converted, print an error message and exit the program
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

