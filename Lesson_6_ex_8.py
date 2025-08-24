print("Lesson 6. Home task №8.")
"""
8. Реализовать функцию, которая находит минимальный и
максимальный элементы в матрице (матрица M x N). Вывести в
консоль индексы найденных элементов.
"""

def search_min_max_in_my_matrix(matr):
    # Принимаем за минимальный элемент в матрице
    min_value = matr[0][0]
    # Принимаем за максимальный элемент в матрице
    max_value = matr[0][0]
    # Позиция минимального элемента в матрице
    min_position = (0, 0)
    # Позиция максимального элемента в матрице
    max_position = (0, 0)

    for i in range(0, len(matr)):
            for j in range(0, len(matr[0])):
    # Проверяемый элемент "x"
                x = matr[i][j]
                if x < min_value:
                    min_value = x
                    min_position = (i, j)
                elif x > max_value:
                    max_value = x
                    max_position = (i, j)

    print(f"Индексы минимального элемента {min_value}:", min_position)
    print(f"Индексы максимального элемента {max_value}:", max_position)




matr = [[10, 1, 5], [-1, 2, 8], [90, 4, 715]]
print(matr)
print(search_min_max_in_my_matrix(matr))





# def find_min_max_indices(matrix):
#     m = len(matrix)  # Количество строк
#     n = len(matrix[0])  # Количество столбцов
#
#     # Найти глобально минимальный и максимальный элементы
#     min_val = float('inf')
#     max_val = float('-inf')
#
#     for row in matrix:
#         for val in row:
#             if val < min_val:
#                 min_val = val
#             if val > max_val:
#                 max_val = val
#
#     # Теперь собираем все индексы минимальных и максимальных элементов
#     min_positions = []
#     max_positions = []
#
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == min_val:
#                 min_positions.append((i, j))
#             if matrix[i][j] == max_val:
#                 max_positions.append((i, j))
#
#     print("Индексы минимальных элементов:", min_positions)
#     print("Индексы максимальных элементов:", max_positions)
#
#
# # Пример использования
# matrix = [
#     [1, 3, 5],
#     [6, 1, 8],
#     [9, 4, 1]
# ]
#
# find_min_max_indices(matrix)