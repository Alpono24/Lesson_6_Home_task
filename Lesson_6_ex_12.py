print("Lesson 6. Home task №12.")
"""
12. Программа получает на вход число H. Реализовать
функцию, которая определяет, какие столбцы имеют хотя бы одно
такое же число, а какие не имеют (матрица M x N).
"""

# Исходная матрица для вычислений
a_m_n = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print("Исходная матрица для вычислений: ", a_m_n)
h = int(input("Введите число Н для поиска в матрице: "))


def find_col_with_h(a_m_n, h):
    m = len(a_m_n)  # строки
    n = len(a_m_n[0])  # столбцы
    col_with_h = []  # список номеров столбцов с Н
    col_without_h = []  # список номеров столбцов с без Н

    for j in range(n):
        success = False
        for i in range(m):
            if a_m_n[i][j] == h:
                success = True
                break
        if success == True:
            col_with_h.append(j + 1)
        else:
            col_without_h.append(j + 1)

    return col_with_h, col_without_h


col_with_h, col_without_h = find_col_with_h(a_m_n, h)

print("Столбцы, содержащие число:", col_with_h)
print("Столбцы, не содержащие число:", col_without_h)
