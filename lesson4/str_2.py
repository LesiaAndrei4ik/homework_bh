'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''
# Запрашиваем числа
numbers = input('Введите несколько чисел через пробел:')

# преобразуем в список чисел
nums = list(map(int, numbers.split()))

total = sum(nums)
maximum = max(nums)
average = total / len(nums) if nums else 0

print('Сумма чисел:', total)
print('Максимальное число:', maximum)
print('Среднее арифметическое:', average)