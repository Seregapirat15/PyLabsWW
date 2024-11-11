import sys

def input_coefficient(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Некорректное значение. Пожалуйста, введите коэффициент еще раз.")

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def calculate_roots(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2*a)]
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return [root1, root2]

def main():
    if len(sys.argv) == 4:
        a, b, c = map(float, sys.argv[1:])
    else:
        a = input_coefficient("Введите коэффициент A: ")
        b = input_coefficient("Введите коэффициент B: ")
        c = input_coefficient("Введите коэффициент C: ")

    discriminant = calculate_discriminant(a, b, c)
    roots = calculate_roots(a, b, c)

    print("Дискриминант:", discriminant)
    if roots:
        print("Корни уравнения:", roots)
    else:
        print("Уравнение не имеет действительных корней.")

if __name__ == "__main__":
    main()