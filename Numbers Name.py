#Number Names - Show how to spell out a number in English.
#You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's
#default bounded integer type, if that's less).
#Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).

# Dictionaries
# The ones values i.e. 0 to 9
ones = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
# The tens values 10 t0 19
tens = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen",
        8: "Eighteen",
        9: "Nineteen"}
# The tens values 10 t0 19
tees = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty",
        9: "Ninety"}

"""
 This function creates a list which stores the number to be converted.
 Gets the length of the input and minus it from 12, to determine how much padding is needed. 
 Add 0's as padding to the list and then append the number entered to list. 

 Args: 
    number: The numerical number the user entered 

 Returns:
    A list of numbers of length 12
"""


def createnumberlist(number):
    # Initialize the variable the number entered in stored in
    # Store the number entered into a list
    stringOfNumbers = []
    # Get the number of padding needed
    numberOfPadding = 12 - len(number)

    # If the number of padding is greater than 0
    # Add the number of necessary 0's to make the list of length 12
    if numberOfPadding > 0:
        for i in range(numberOfPadding):
            stringOfNumbers.append(0)

    # Add the number entered into the list
    for char in number:
        stringOfNumbers.append(int(char))

    return stringOfNumbers


"""
 This functions determines the tens and ones of value of the number. 
 It compares the two arguments with various if statements and if the statement evaluates to true,
 gets the corresponding word for the number from the dictionaries defined.

 Args:
    num1, num2: Numbers to be checked

 Returns: 
    Return corresponding words 
"""


def getTensofTees(num1, num2):
    # Initialize variables
    teesOrTens = ""

    # Get the teens
    if num1 == 1:
        # 11 to 19
        teesOrTens = tens[num2]
    # Get number in the tees without any ones
    elif num1 > 1 and num2 == 0:
        # 20 to 90
        teesOrTens = tees[num1]
    # Get 0
    elif num1 == 0 and num2 == 0:
        # 0
        teesOrTens = ones[num2]
    # Get the numbers in the tees with ones
    elif num1 > 1 and num2 != 0:
        # 21, 22, .... 99
        teesOrTens = tees[num1] + "-" + ones[num2]
    # Get the ones
    else:
        teesOrTens = ones[num2]

    return teesOrTens


"""
 This functions combine the number . 
 It compares the two arguments with various if statements and if the statement evaluates to true,
 gets the corresponding word for the number from the dictionaries defined.

 Args:
    num1, num2: Numbers to be checked

 Returns: 
    Return corresponding words 
"""


def getHundred(num, num1, num2):
    # Initialized variables
    words = ""

    # The is no hundred value
    if num == 0:
        # Get the tens and ones
        words = getTensofTees(num1, num2)
    # If there is a hundred value and also tens and ones
    if num != 0 and (num1 > 0 or num2 > 0):
        # Get the hundredths, and teens or ones or tees
        words = ones[num] + " hundred and " + getTensofTees(num1, num2)

    # If there is hundred and no tens or ones
    if num != 0 and num1 == 0 and num2 == 0:
        # Get the hundredths
        words = ones[num] + " hundreds"

    return words


"""
 This function takes a string entered by the user, calls the function createnumberlist to convert the string into a list of numbers.
 Declare and initialize variables for index and numberinwords. The variable index is used to go through the list of numbers
 and the variable numberinwords stores each word representing the number in the list. A while loop is used to traverse the list of numbers. 
 Each iteration of the while loop compares three values from the number list at a time. The first iteration determines if there are billions, 
 second checks if there are millions, and third if there are thousands, in the number entered. Then the last three indexes values are checked
 which represents the hundredths, tenths and ones. 

 Args:
    number: Value the user entered

 Returns:
    numberinwords: Words representing the number the user entered. 
"""

def getWords(number):
    # Convert the number entered into a list of length 12
    numberlist = createnumberlist(number)

    # Initialize variables
    index = -1
    numberinwords = ""

    # Run while index is less than 12
    while index < len(numberlist) - 1:
        # Increase index by 3
        index += 3
        # Check if index is 0 to 2
        if (index - 2 == 0 and numberlist[index - 2] != 0) or (index - 1 == 1 and numberlist[index - 1] != 0) or (
                index == 2 and numberlist[index] != 0):
            # Get the corresponding words for the numbers at each index
            numberinwords += getHundred(numberlist[index - 2], numberlist[index - 1], numberlist[index]) + " billion "
            # Start over the loop
            continue
        # Check if the index 3 to 5
        if (index - 2 == 3 and numberlist[index - 2] != 0) or (index - 1 == 4 and numberlist[index - 1] != 0) or (
                index == 5 and numberlist[index] != 0):
            # Get the corresponding words for the numbers at each index
            numberinwords += getHundred(numberlist[index - 2], numberlist[index - 1], numberlist[index]) + " million "
            # Start over the loop
            continue
        # Check if the 6  to 8
        if (index - 2 == 6 and numberlist[index - 2] != 0) or (index - 1 == 7 and numberlist[index - 1] != 0) or (
                index == 8 and numberlist[index] != 0):
            # Get the corresponding words for the numbers at each index
            numberinwords += getHundred(numberlist[index - 2], numberlist[index - 1], numberlist[index]) + " thousand "
            # Start over the loop
            continue

        # Check the last three indexes
        if numberlist[index - 2] == 0 and (
                (numberlist[index - 1] != 0 or numberlist[index] != 0) and len(numberinwords) != 0):
            # If there is no hundred value and there are tens or ones and there is value store in numberinwords already
            numberinwords += " and " + getHundred(numberlist[index - 2], numberlist[index - 1], numberlist[index])
        elif numberlist[index - 2] == 0 and numberlist[index - 1] == 0 and numberlist[index] == 0:
            # If there is no hundred, tens or ones
            numberinwords += numberinwords
        else:
            # If there is hundreds, tens and ones
            numberinwords += getHundred(numberlist[index - 2], numberlist[index - 1], numberlist[index])

    return numberinwords + "."


# Get number from user
continues = 'Y'
while continues.capitalize() == 'Y':
    number = input("Enter number from 0 to 999999999999------->  ")
    print(f"Number {number} is {getWords(number)}")
    continues = input("Do you want to continue: (Y or N)------>  ")
