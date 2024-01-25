import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Помилка: Неправильні вхідні значення")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Помилка: Неможливо ділити на нуль.")
    # exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")