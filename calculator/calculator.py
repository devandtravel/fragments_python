error_message = "Division by 0!"
output = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
    "mod": lambda x, y: x % y,
    "pow": lambda x, y: x**y,
    "div": lambda x, y: x // y
}
number1 = float(input())
number2 = float(input())
operator = input()
try:
    print(output[operator](number1, number2))
except ZeroDivisionError:
    if (number2 == 0) and operator in ("/", "mod", "div"):
        print(error_message)
