# Worksheet 1.2: Task 2 Solution

import sys

try:
    #*get the user to enter a sequence of floats, with a specific character in between so i can
    #*seperate the values into a list
    seq = input("Please enter a sequence of float numbers, separated by a single space \n")

    #*create a list of floats by splitting the input string at the spaces
    floatList = seq.split(" ")

    #*convert the list of string into a list of floats
    floatList = [float(i) for i in floatList]

    #*sort the list in ascending order
    floatList.sort()

    listSize = len(floatList)

    #*get the minimum value from the list
    minValue = floatList[0]

    #*get the maximum value from the list 
    maxValue = floatList[listSize - 1]

    #*add every value in the list together
    total = 0
    for i in range(len(floatList)):
        if i == 0:
            total = floatList[i]
        else:
            total = total + floatList[i]

    #*calculate the mean value
    mean = total / listSize

    #*calculate the median value
    medianIndex = listSize // 2

    #*if there is two numbers in the middle, add them and divide by two
    if medianIndex % 2 == 0 or listSize == 2:
        median = (floatList[medianIndex-1] + floatList[medianIndex]) / 2
    else:
        median = floatList[medianIndex]

    #*print out all the calculated values
    print(f"Minimum = {minValue}")
    print(f"Maximum = {maxValue}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")

except:
    sys.exit("Error: no numbers provided")
