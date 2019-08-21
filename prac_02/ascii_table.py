LOWER = 33
UPPER = 137


def main():
    character_input = input("Enter a character: ")
    while len(character_input) > 1 or 0 >= len(character_input):
        character_input = input("Enter a character: ")
    ascii_code = ord(character_input)
    print("The ASCII code for {0} is {1}".format(character_input, ascii_code))
    valid_input = False
    while not valid_input:
        try:
            number_input = int(input("Enter a number between {0} and {1}: ".format(LOWER, UPPER)))
            while number_input > UPPER or LOWER > number_input:
                number_input = int(input("Enter a number between {0} and {1}: ".format(LOWER, UPPER)))
            character = chr(number_input)
            valid_input = True
        except ValueError:
            print("Value Error:")
    print("The character for {0} is {1}".format(number_input, character))


main()
