print("Lesson 6. Home task №1.")
"""
1. Дан список чисел, отсортированных по возрастанию. На
вход принимается значение, равное одному из элементов списка.
Реализовать функцию, выполняющую рекурсивный алгоритм
бинарного поиска, на выходе программа должна вывести позицию
искомого элемента в исходном списке.
"""


def search_index_position(my_list, element_to_search, left=0, right=None):
    # left - индекс левой границы
    # right - индекс правой границы

    # Определение индекса правой границы
    if right is None:
        right = len(my_list) - 1

    # Если левая граница больше правой, значит элемент отсутствует
    if left > right:
        return -1

    # Определение средней точки
    mid = (left + right) // 2

    # Проверка среднего элемента
    if my_list[mid] == element_to_search:
        return mid
    elif my_list[mid] < element_to_search:
        return search_index_position(my_list, element_to_search, mid + 1, right)  # искать справа
    else:
        return search_index_position(my_list, element_to_search, left, mid - 1)  # искать слева


a_lst = [1, 3, 5, 7, 9, 11, 13, 15]
b_el = 11
res = search_index_position(a_lst, b_el, 0)

if res != -1:
    print(f"Элемент {b_el} найден на позиции {res}")
else:
    print(f"Элемент {b_el} не найден")