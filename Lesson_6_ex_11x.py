print("Lesson 6. Home task №11*.")
"""
11*. Реализовать функцию, которая суммирует элементы
каждой строки матрицы с соответствующими элементами L-й строки
(матрица M x N)
"""

def sum_el_amn_l_row(a_m_n, l):
    # Проверяем корректность индекса строки
    if not a_m_n or len(a_m_n) <= l:
        raise ValueError("Индекс строки вне границ матрицы")

    # Количество строк в матрице
    m = len(a_m_n)
    # Количество столбцов в матрице
    n = len(a_m_n[0])
    # Матрица для результата
    result_a_m_n = []

    for i in range(m):
    # Матрица для суммы ряда
        row_sums = []

    # Если текущая строка равна строке l, копируем её и значения оставляем без изменений
        if i == l:
            row_sums.extend(a_m_n[i])
        else:
    # Складываем каждый элемент текущей строки с соответствующим элементом строки l
            for j in range(n):
                row_sums.append(a_m_n[i][j] + a_m_n[l][j])
        result_a_m_n.append(row_sums)
    return result_a_m_n



a_m_n = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]
l = int(input("Введите индекс ряда: "))
result = sum_el_amn_l_row(a_m_n, l)
print(result)
