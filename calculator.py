while True:
    num1, operator, num2 = input("Введіть приклад: ").split()

    try:
        num1 = float(num1)
        num2 = float(num2)
    except(ValueError):
        print("Ви ввели не число")
        exit()

    if operator == "+":
        print(round(num1 + num2, 2))
    elif operator == "-":
        print(round(num1 - num2, 2))
    elif operator == "*":
        print(round(num1 * num2, 2))
    elif operator == "/":
        try:
            print(round(num1 / num2, 2))
        except(ZeroDivisionError):
            print("Ділення на 0")
    elif operator == "**":
        print(round(num1 ** num2, 2))
    elif operator == "//":
        try:
            print(round(num1 // num2, 2))
        except(ZeroDivisionError):
            print("Ділення на 0")
    elif operator == "%":
        try:
            print(round(num1 % num2, 2))
        except(ZeroDivisionError):
            print("Ділення на 0")
    else:
        print('Вибачте але оператор ',operator, "покищо не підтримується")