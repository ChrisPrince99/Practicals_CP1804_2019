"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
"""


def main():
    """Display income report for incomes over a given number of months."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = []

    for number in range(5):
        number_to_add = float(input("Enter number {}: ".format(number + 1)))
        numbers.append(number_to_add)

    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_of_numbers = (sum(numbers) / 5)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[4]))
    print("The smallest number is {}".format(smallest_number))
    print("The largest number is {}".format(largest_number))
    print("The average of the numbers is {}".format(average_of_numbers))

    """
    Ask the user for their username. If the username is in the above list of authorised users,
    print "Access granted", otherwise print "Access denied".
    """

    username = input("Please enter your username (Case sensetive): ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
