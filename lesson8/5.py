'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''


def count_char(input_string):
    # Создаем пустой словарь для хранения результатов (символы строки и их частоту)
    char_count = {}
    
    # Перебираем каждый символ в строке
    for char in input_string:
        # Если символ уже есть в словаре (if char in char_count), то увеличиваем его значение на 1
        if char in char_count:
            char_count[char] += 1
        else:
            # Если символа нет в словаре, добавляем его с начальным значением 1
            char_count[char] = 1
    
    # Возвращаем словарь с результатом
    return char_count

# Пример использования
input_string = "helloooo"
result = count_char(input_string)
print(result)