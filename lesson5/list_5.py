'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

list = ['samsung', 'lg', 'xerox', 'bosch']

# удаляем xerox. remove удаляет эл-т по имени
list.remove('xerox')

# добавляем indesit на 2 место (индекс 1)
list.insert(1, 'indesit')

print(list)