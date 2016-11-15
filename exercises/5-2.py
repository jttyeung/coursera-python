# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")

    try : int(num) # Error checking
    except :
        print "Invalid input"

    if num == "done" : break
    elif smallest == None : smallest = int(num)  # Need to add smallest == None, otherwise "None" (nonexistent) is always "smaller" than anything in existence. Fixed/updated in Python 3.
    elif int(num) > largest : largest = int(num)
    elif int(num) < smallest : smallest = int(num)


print "Maximum is", largest
print "Minimum is", smallest