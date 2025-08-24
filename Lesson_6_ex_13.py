print("Lesson 6. Home task №13.")
"""
13. Реализовать функцию, которая находит сумму элементов
на главной диагонали и сумму элементов на побочной диагонали
(матрица M x N)
"""


def diоganal_summs(a_m_n):
    if not a_m_n or len(a_m_n) != len(a_m_n[0]):
        raise ValueError("Матрица должна быть квадратной")
    else:
        main_diagonal_sum = 0
        for i in range(len(a_m_n)):
            main_diagonal_sum += a_m_n[i][i]
        secondary_diagonal_sum = 0
        for j in range(len(a_m_n)):
            secondary_diagonal_sum += a_m_n[j][len(a_m_n) - j - 1]
        return main_diagonal_sum, secondary_diagonal_sum


a_m_n = [
    [1, 2, 3, 4],
    [5, 6, 7, 8, 5],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
main_diagonal_sum, secondary_diagonal_sum = diоganal_summs(a_m_n)

print(f"Сумма элементов главной диагонали: {main_diagonal_sum}")
print(f"Сумма элементов побочной диагонали: {secondary_diagonal_sum}")
