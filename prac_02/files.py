

user_name = input("Please enter your name: ")
output_file = open('name.txt', 'w')

print(user_name, file=output_file)
output_file.close()

input_file = open("name.txt", "r")
print("Your name is {}".format(input_file.read()))
input_file.close()

input_file = open("numbers.txt", "r")
for i in range(2):
    print(input_file.readline())
input_file.close()

input_file = open("numbers.txt", "r")
total = 0
for line in input_file:
    print(line)
    total += int(line)
print(total)
input_file.close()

