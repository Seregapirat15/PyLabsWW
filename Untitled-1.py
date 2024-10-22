def calculate_expression():
    s = str(input()).split()
    a = float(s[0])
    b = float(s[2])
    result = 0
    
    if s[1] == '+':
        result = (a + b)
    elif s[1] == '-':
        result = (a - b)
    elif s[1] == '*':
        result = (a * b)
    elif s[1] == '/':
        if b == 0:
            print("Деление на ноль невозможно.")
            return
        result = (a / b)
    elif s[1] == '%':
        if b == 0:
            print("Деление на ноль невозможно.")
            return
        result = (a % b)
    else:
        print('Неверная операция.')
        return

    result = round(result, 2)

    print(f"Результат: {result}")

calculate_expression()