# A shop requires a small program that would allow them to quickly work
# out the total price for a number of items, each with different prices.
#
# The program allows the user to enter the number of items and the price of each different item.
# Then the program computes and displays the total price of those items.
# If the total price is over $100, then a 10% discount is applied
# to that total before the amount is displayed on the screen.
number_of_items = int(input("Please enter the number of items to be calculated for: #"))
while 0 > number_of_items:
    print("Error: invalid input")
    number_of_items = int(input("Please enter the number of items to be calculated for: #"))
total = 0
total_discount = 0
print("Number of Items:", number_of_items)
for i in range(number_of_items):
    price_of_item = int(input("Please enter the price of item number " + str(i + 1) + " "))
    print("Price for item {0} is: ".format((i + 1)), price_of_item)
    total += price_of_item
if total > 100:
    total_discount = total * 0.10

total -= total_discount

print("Total price for", number_of_items, "items:", total)
