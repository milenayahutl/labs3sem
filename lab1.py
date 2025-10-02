import sys
import math

def get_coef(index, prompt):
    while True:
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()

        try:
            coef = float(coef_str)
            return coef
        except ValueError:
            print("Ошибка: введите действительное число")
            # Если была ошибка в командной строке, сбрасываем индекс
            # чтобы перейти к вводу с клавиатуры
            if index < len(sys.argv):
                index = len(sys.argv) + 1


def solve_biquadratic(a, b, c):
    if a == 0:
        print("коэффициент A не может быть равен 0 для биквадратного уравнения")
        return []

    D = b * b - 4 * a * c
    roots = []

    if D < 0.0:
        return roots
    elif D == 0.0:
        t = -b / (2.0 * a)
        if t > 0:
            root1 = math.sqrt(t)
            root2 = -math.sqrt(t)
            roots.extend([root1, root2])
        elif t == 0:
            roots.append(0.0)
    else:
        t1 = (-b + math.sqrt(D)) / (2.0 * a)
        t2 = (-b - math.sqrt(D)) / (2.0 * a)

        if t1 > 0:
            root1 = math.sqrt(t1)
            root2 = -math.sqrt(t1)
            roots.extend([root1, root2])
        elif t1 == 0:
            roots.append(0.0)

        if t2 > 0:
            root3 = math.sqrt(t2)
            root4 = -math.sqrt(t2)

            if not (t2 == 0 and 0.0 in roots):
                roots.extend([root3, root4])
        elif t2 == 0 and 0.0 not in roots:
            roots.append(0.0)

    # Убираем возможные дубликаты и сортируем
    roots = sorted(list(set(roots)))
    return roots


def main():

    print("Решение биквадратного уравнения: A*x^4 + B*x^2 + C = 0")

    a = get_coef(1, 'Введите коэффициент A:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = solve_biquadratic(a, b, c)

    print(f"\nУравнение: {a}*x^4 + {b}*x^2 + {c} = 0")

    len_roots = len(roots)
    if len_roots == 0:
        print('Действительных корней нет')
    elif len_roots == 1:
        print('Один действительный корень: {:.6g}'.format(roots[0]))
    elif len_roots == 2:
        print('Два действительных корня: {:.6g} и {:.6g}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три действительных корня: {:.6g}, {:.6g} и {:.6g}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре действительных корня: {:.6g}, {:.6g}, {:.6g} и {:.6g}'.format(roots[0], roots[1], roots[2], roots[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()