class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_roots(self):
        dis = self.b**2 - 4*self.a*self.c
        if dis < 0:
            return []
        elif dis == 0:
            return [-self.b / (2*self.a)]
        else:
            root1 = (-self.b + dis**0.5) / (2*self.a)
            root2 = (-self.b + dis**0.5) / (2*self.a)
            return [root1, root2]
        
    def print_roots(self):
        roots = self.calculate_roots()
        if roots:
            print("Корни уравнения:", roots)
        else:
            print("Уравнение не имеет действительных корней.")
    
def main():
    a = float(input("Введите коэффициент A: "))
    b = float(input("Введите коэффициент B: "))
    c = float(input("Введите коэффициент C: "))
        
    equation = QuadraticEquation(a, b, c)       
    equation.print_roots()

if __name__ == "__main__":
    main()