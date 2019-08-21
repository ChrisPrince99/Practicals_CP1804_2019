"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? - if anything other than a number is inputted
2. When will a ZeroDivisionError occur? - if either of the numbers inputted are 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? - Yes by using two while loops to prevent
0 being used for either input
"""

try:
    numerator = int(input("Enter the numerator: "))
    while numerator == 0:
        numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
