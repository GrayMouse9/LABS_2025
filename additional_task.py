import sys
import math


class BiquadraticEquation:
    def __init__(self, a: float, b: float, c: float):
        """Конструктор класса — сохраняем коэффициенты уравнения"""
        if a == 0:
            raise ValueError("Коэффициент A не может быть равен 0 для биквадратного уравнения")
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self) -> float:
        """Вычисляем дискриминант квадратного уравнения относительно y = x^2"""
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        """Решение биквадратного уравнения: возвращает список действительных корней"""
        roots = []
        D = self.discriminant()

        if D < 0:
            return roots

        if abs(D) < 1e-12:  # считаем, что дискриминант равен 0
            y = -self.b / (2 * self.a)
            if y >= 0:
                roots.append(math.sqrt(y))
                roots.append(-math.sqrt(y))
        else:
            sqD = math.sqrt(D)
            y1 = (-self.b + sqD) / (2 * self.a)
            y2 = (-self.b - sqD) / (2 * self.a)
            for y in (y1, y2):
                if y >= 0:
                    roots.append(math.sqrt(y))
                    roots.append(-math.sqrt(y))

        return sorted(set(roots))

    def __str__(self):
        """Строковое представление уравнения"""
        return f"{self.a}*x^4 + {self.b}*x^2 + {self.c} = 0"


def get_coef(index, prompt):
    """Чтение коэффициента из argv или ввода"""
    if index < len(sys.argv):
        try:
            return float(sys.argv[index])
        except ValueError:
            print(f"Некорректный аргумент: {sys.argv[index]}. Введите вручную.")
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: нужно ввести число.")


def main():
    # Читаем коэффициенты
    a = get_coef(1, "Введите коэффициент A: ")
    b = get_coef(2, "Введите коэффициент B: ")
    c = get_coef(3, "Введите коэффициент C: ")

    try:
        eq = BiquadraticEquation(a, b, c)
    except ValueError as e:
        print("Ошибка:", e)
        return

    print("Уравнение:", eq)
    roots = eq.solve()

    if not roots:
        print("Действительных корней нет")
    elif len(roots) == 1:
        print("Один действительный корень:", roots[0])
    else:
        print("Действительные корни:", ", ".join(map(str, roots)))


if __name__ == "__main__":
    main()
