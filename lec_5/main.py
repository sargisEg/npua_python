def sum_of_elements(numbers, exclude_negative=False):
    num_sum = 0
    for number in numbers:
        if not exclude_negative or (exclude_negative and number >= 0):
            num_sum += number
    return num_sum

numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in numbers.split()]

exclude_negative = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()
exclude_negative = exclude_negative == "yes"

num_sum = sum_of_elements(numbers, exclude_negative)

if exclude_negative:
    print("Sum of non-negative numbers:", num_sum)
else:
    print("Sum of all numbers:", num_sum)
