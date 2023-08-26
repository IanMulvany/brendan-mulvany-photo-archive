# Given numbers
numbers = []

# read the list of numbers from numbers.txt, and convert them to ints, and put them in a list
with open('roll-numbers.txt', 'r') as f:
    for line in f:
        numbers.append(int(line.strip()))

# Grouping numbers by their first digit
grouped_numbers = {}
for num in numbers:
    first_digit = str(num)[0]
    if first_digit not in grouped_numbers:
        grouped_numbers[first_digit] = []
    grouped_numbers[first_digit].append(num)

# for each key in grouped_numbers, if the key is 1, or the key is 2, group the numbers by their second digit, and sort them

for key in grouped_numbers:
    if key == '1' or key == '2':
        # Sorting by the whole number after considering the second digit
        grouped_numbers[key] = sorted(grouped_numbers[key], key=lambda x: (str(x)[1], x) if len(str(x)) > 1 else (str(x)[0], x))
    else:
        grouped_numbers[key] = sorted(grouped_numbers[key])


for key, value in grouped_numbers.items():
    print(key, value)
    print("\n\n")