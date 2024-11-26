#1.You have been given a python list[10,501,22,37,100,999,87,351] your task is to create two list one which have all the even numbers and another list which will have all the oddd numbers in it

# numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# List of odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Printing the lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# List of odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Printing the lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# Define the list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List of even numbers (those divisible by 2)
even_numbers = [num for num in numbers if num % 2 == 0]

# List of odd numbers (those not divisible by 2)
odd_numbers = [num for num in numbers if num % 2 != 0]

# Printing the lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
