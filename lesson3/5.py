'''
Запросить количество секунд. 
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.

'''
# вариант 1 без форматной строки

seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
min = (seconds % 3600) // 60
secs = seconds % 60

print(hours, ":", min, ":", secs)



# вариант 2 с форматной строкой

seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

# добавляем 0, если число меньше 10
if hours < 10:
    hours = "0" + str(hours)
else:
    hours = str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)

if secs < 10:
    secs = "0" + str(secs)
else:
    secs = str(secs)

print(hours + ":" + minutes + ":" + secs)