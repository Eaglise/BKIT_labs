# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()

    while(True):
        # Пробуем перевести строку в действительное число
        try: coef = float(coef_str)
        except: print("Попробуйте ещё раз:")
        else: return coef
        coef_str = input()


def get_roots(a, b, c):
    '''
    Вычисление корней биквадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    if a == 0.0:
        if b == 0 and c == 0: result = [1,2,3,4,5]
        elif b == 0.0: result = [1,2,3,4,5,6]
        elif c == 0.0: result.append(0.0)
        else:
            root = -c/b
            if root > 0.0:
                result.append(math.sqrt(-c/b), -math.sqrt(-c/b))
    else:
        D = b * b - 4 * a * c
        if D == 0.0:
            root = -b / (2.0 * a)
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0 * a)
            root2 = (-b - sqD) / (2.0 * a)
            if root1 > 0.0:
                result.append(math.sqrt(root1))
                result.append(-math.sqrt(root1))
            if root2 > 0.0:
                result.append(math.sqrt(root2))
                result.append(-math.sqrt(root2))
            if root1 == 0 or root2 ==0: result.append(0.0)
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет рациональных корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    elif len_roots == 5:
        print('Бесконечное множетсво решений')
    elif len_roots == 6:
        print('х = пустое множество')

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()


