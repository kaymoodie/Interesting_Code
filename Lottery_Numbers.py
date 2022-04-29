from Modules import Linked_List_Class
from random import randint

# Declare a variable for storing all the lottery numbers
lottery_numbers = Linked_List_Class.Linked_List()

# Set how many numbers to be created
start = 1
end = 37
# Create a list of numbers
numbers = [num for num in range(start, end)]

# Store the numbers created in a linked list
lottery_numbers.get_data_values(numbers)
lottery_numbers.create_list()

# Initialize variables
# Amount of numbers to be created
index = 1
# Store the numbers
results = []

# Get 1 to 6 numbers
while index <= 6:
    while True:
        # Random select a number between 1 and 36
        lottery_number_pick = lottery_numbers.get_a_node(randint(start, end-1))
        # If number exists
        if lottery_number_pick is not None:
            # Add number to the results variable
            results.append(lottery_number_pick.data)
            # Delete the number found from the list
            lottery_numbers.delete_a_node(lottery_number_pick)
            # Exit the inner loop
            break
    # Go to the next index
    index += 1

# Sort the numbers in ascending order
results.sort()

# Display each number generated
for index, number in enumerate(results, 1):
    print(f"Number {index}: {number}")


# Get the powerball
# Select a random number between 1 and 9
powerball = randint(1, 9)
print(f"Powerball: {powerball}")




