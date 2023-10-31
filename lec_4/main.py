def classify_numbers(numbers):
    evens = []
    odds = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    return evens, odds

numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in numbers.split()]

evens, odds = classify_numbers(numbers)

print("Even numbers:", evens)
print("Odd numbers:", odds)
