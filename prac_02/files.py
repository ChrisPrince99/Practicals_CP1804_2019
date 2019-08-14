

user_name = input("Please enter your name: ")
out_file = open('name.txt', 'w')

print(user_name, file=out_file)
out_file.close()

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    print(line)
    total += int(line)
print(total)
in_file.close()
