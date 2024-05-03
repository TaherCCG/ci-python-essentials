
# Create a list of numbers and then create a new list that contains only the numbers that are greater than 40

all_numbers=[1, 5, 44, 22, 13, 17, 56, 3, 88, 9, 97]

big_numbers = []

for number in all_numbers:
    if number > 40:
        big_numbers.append(number)

print(all_numbers)
print(big_numbers)
