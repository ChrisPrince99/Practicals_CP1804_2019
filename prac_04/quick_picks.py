import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():

    number_to_generate = int(input("Please enter the number of random number lines you wish to generate: "))
    for number in range(number_to_generate):
        numbers = []
        for number_inline in range(NUMBERS_PER_LINE):
            number_line = random.randrange(MIN_NUMBER, MAX_NUMBER)
            while number_line in numbers:
                number_line = random.randrange(MIN_NUMBER, MAX_NUMBER)
            numbers.append(number_line)
        numbers.sort()
        print(" ".join("{:2}".format(number) for number in numbers))


main()
