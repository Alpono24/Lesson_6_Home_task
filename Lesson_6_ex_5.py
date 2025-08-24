print("Lesson 6. Home task №5.")
"""
5. Программа получает на вход строку – сообщение и
указание, что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное сообщение
шифром Цезаря, вторая – расшифровывает. В зависимости от
выбора пользователя (шифровать или дешифровать) вызывается
соответствующая функция, результат выводится в консоль.
"""


def encrypt_cezar(string, k):
    encrypted = []
    for char in string:
    # Проверяем содержит ли наша строка только буквенные символы
        if char.isalpha():
    # Определяем позицию символа в алфавите ('А' или 'а')
            base = ord('А') if char.isupper() else ord('а')
    # Вычисляем новую позицию символа после сдвига
            new_position = ((ord(char) - base + k) % 32)
    # Преобразуем обратно в символ и добавляем в список
            encrypted.append(chr(base + new_position))
        else:
    # Нечувствительные символы остаются неизменными
            encrypted.append(char)
    return ''.join(encrypted)

def decrypt_cezar(ciphered_text, k):
    decrypted = []
    for char in ciphered_text:
        if char.isalpha():
    # Определяем позицию символа в алфавите ('А' или 'а')
            base = ord('А') if char.isupper() else ord('а')
    # Вычисляем старую позицию символа перед сдвигом
            old_pos = ((ord(char) - base - k) % 32)
    # Преобразуем обратно в символ и добавляем в список
            decrypted.append(chr(base + old_pos))
        else:
    # Нечувствительные символы остаются неизменными
            decrypted.append(char)
    return ''.join(decrypted)



string = input("Введите сообщение: ")
choice = int(input("Выберите режим (1 - шифрование/2 - дешифрование): "))  # Шифровать / Дешифровать
k = int(input("Введите число k - значение сдвига: "))

if choice == 1:
        result = encrypt_cezar(string, k)
        print(f"Зашифрованное сообщение: {result}")
elif choice == 2:
        result = decrypt_cezar(string, k)
        print(f"Дешифрованное сообщение: {result}")
else:
        print("Ошибка выбора режима.")







# Старый код. До знакомства с функциями char() и ord(). Не работает в полной мере с последними знаками
# def my_enigma_simple_encryption(string):
#     string_list = list(string)
#     for i in range(0, len(string)):
#         for j in range(0, len(alphabet)):
#
#             if j + k <= len(alphabet):
#                 if string[i] == alphabet[j]:
#                     string_list[i] = alphabet[j + k]
#
#             if j + k > len(alphabet):
#                 if string[i] == alphabet[j]:
#                     j = 0
#                     string_list[i] = alphabet[j + k]
#             else:
#                 continue
#     return ("".join(string_list))
#
#
# def my_enigma_simple_decryption(string):
#     string_list = list(string)
#     for i in range(0, len(string)):
#         for j in range(0, len(alphabet)):
#
#             if j + k <= len(alphabet):
#                 if string[i] == alphabet[j]:
#                     string_list[i] = alphabet[j - k]
#
#             if j + k > len(alphabet):
#                 if string[i] == alphabet[j]:
#                     j = 0
#                     string_list[i] = alphabet[j - k]
#
#
#
#
#             # if string[i] == alphabet[j]:
#             #     string_list[i] = alphabet[j - k]
#             #
#
#             else:
#                 continue
#     return ("".join(string_list))
#
#
# alphabet = ["a", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
#             "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю"]
# string = input(f"Введите сообщение: ")
# k = int(input(f"Введите число k - значение сдвига: "))
#choice = int(input("""Введите цифру 1 чтобы выполнить шифрование текста или цифру 2 чтобы выполнить дешифрование текста:"""))
#
# if choice == 1:
#     print("Вы ввели цифру 1, будет выполнено шифрование введенного текста!!!")
#     print(f"Сообщение \"{string}\" зашифровано как: \"{my_enigma_simple_encryption(string)}\".")
# elif choice == 2:
#     print("Вы ввели цифру 2, будет выполнено дешифрование введенного текста!!!")
#     print(f"Сообщение \"{string}\" зашифровано как: \"{my_enigma_simple_decryption(string)}\".")