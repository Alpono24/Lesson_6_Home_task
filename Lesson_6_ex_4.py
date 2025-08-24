print("Lesson 6. Home task №4.")
"""
4. Программа получает на вход два числа и находит их
НОД (наибольший общий делитель). Пример: на вход
подаются числа 12 и 18, их НОД равен 6.
"""

def all_divisors(num1: int, num2: int) -> list:

    # создаем список для всех делителей первого числа
    divisors_num1 = []

    # Наполняем список всеми делителями первого числа
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisors_num1.append(i)

    # создаем список для всех делителей второго числа
    divisors_num2 = []

    # Наполняем список всеми делителями второго числа
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            divisors_num2.append(i)

    # создаем список общих делителей для двух чисел
    com_div = []
    # Наполняем список всеми общими делителями двух чисел
    for i in range(0, len(divisors_num1)):
        for j in range(0, len(divisors_num2)):
            if divisors_num1[i] == divisors_num2[j]:
                com_div.append(divisors_num1[i])
            elif divisors_num1[i] != divisors_num2[j]:
                continue
            else:
                break

    print(f"Вывод всех делителей первого введенного числа {num1} в список: {divisors_num1}. Общее количество делителей {len(divisors_num1)}.")
    print(f"Вывод всех делителей второго введенного числа {num2} в список: {divisors_num2}. Общее количество делителей {len(divisors_num2)}.")
    print(f"Вывод всех общих делителей чисел {num1} и {num2} в список: {com_div}")
    # Находим наибольший общий делитель из общих делителей -> НОД
    print(f"Вывод наибольшего общего делителя (НОД) чисел {num1} и {num2} из списка {com_div}: {max(com_div)} ")

num1  = int(input("Введите первое число: "))
num2  = int(input("Введите второе число: "))
all_divisors(num1, num2)
