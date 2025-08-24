print("Lesson 6. Home task №10*.")
"""10*. Реализовать функцию, которая перемножает элементы
каждого столбца матрицы с соответствующими элементами K-го
столбца (матрица M x N).
"""

a_m_n = [
    [1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3]
]
print("Исходная матрица для вычислений: ", a_m_n)
k = int(input(f"Введите номер столбца в диапазоне от [1,{len(a_m_n[0])}]: "))
if k >= 1 and k <= len(a_m_n):
    print(f"Для умножения выбран столбец {k} c индексом {k-1}")
elif k < 1 or k > len(a_m_n):
    print(f"Номер столбца выходит за диапазон [1,{len(a_m_n[0])}]!!!")



def mult_each_cols_by_el_k_col(a_m_n, k):
    m = len(a_m_n) # Количество строк
    n = len(a_m_n[0]) # Количество столбцов

    k_col_list = []
    for i in range(m):
        k_col_list.append(a_m_n[i][k])

    result = []
    for _ in range(m):
        row = [0]*n
        result.append(row)

    for i in range(m):
        for j in range(n):
            result[i][j] = a_m_n[i][j] * k_col_list[i]
    return result


print(f"Результат умножения: {mult_each_cols_by_el_k_col(a_m_n, k)}")























# def k_number_is(a_m_n):
#     # переводим номер столбца в его индекс
#     k = int(input(f"Введите номер столбца в диапазоне от [1,{len(a_m_n)}]: "))-1
#     # Проверяем условие
#     if k < 0 or k >= len(a_m_n):
#         print(f"Номер столбца выходит за диапазон [1,{len(a_m_n)}]!!!")
#         k_number_is(a_m_n)
#     elif k >= 0 or k < len(a_m_n)-1:
#         print(f"Для умножения выбран столбец {k + 1} c индексом {k}")
#         return int(k)