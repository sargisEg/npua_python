def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Enter one of operations")
print("'add', 'sub', 'mult', 'div'")

operation = input("")
    
result = 0
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    print("Invalid input")
    
print("Result:", result)
