# Exercise1
rate = 9  # Базовая ставка по ипотеке = 9%
region = input('Из какого вы региона?: ')
if region == 'Амурская область' or region == 'Республика Бурятия' or region == 'Якутия':
  rate = 2
  print(f'Ваша ставка по ипотеке = {rate}%')
else:
  children = int(input('Сколько у вас детей?: '))
  salary_p = input('Есть ли у вас зарплатный проект в нашем банке?(Да/Нет): ')
  insurance = input('Будет ли оформлено страхование?(Да/Нет): ')
  if children > 3:
    rate -= 1
  if salary_p == 'Да':
    rate -= 0.5
  if insurance == 'Да':
    rate -= 1.5
  print(f'Ваша ставка по ипотеке = {rate}%')

# Exercise2
month = input('Введите месяц: ')
number = int(input('Введите число: '))
signs = {"март": (21, "Рыбы", "Овен"), "апрель": (21, "Овен", "Телец"), "май": (22, "Телец", "Близнецы"),
        "июнь": (22, "Близнецы", "Рак"), "июль": (23, "Рак", "Лев"), "август": (24, "Лев", "Дева"),
        "сентябрь": (24, "Дева", "Весы"), "октябрь": (24, "Весы", "Скорпион"),
        "ноябрь": (23, "Скорпион", "Стрелец"), "декабрь": (23, "Стрелец", "Козерог"),
        "январь": (21, "Козерог", "Водолей"), "февраль": (20, "Водолей","Рыбы")}
 
 
if (number >= signs[month][0]):
   print(signs[month][2])
else:
   print(signs[month][1])
# if month == 'март' and 21 <= number <= 31 or month == 'апрель' and 1 <= number <= 20:
#   print('Овен')
# elif month == 'апрель' and 21 <= number <= 30 or month == 'май' and 1 <= number <= 21:
#   print('Телец')
# elif month == 'май' and 22 <= number <= 31 or month == 'июнь' and 1 <= number <= 21:
#   print('Близнецы')
# elif month == 'июнь' and 22 <= number <= 30 or month == 'июль' and 1 <= number <= 22:
#   print('Рак')
# elif month == 'июль' and 23 <= number <= 31 or month == 'август' and 1 <= number <= 21:
#   print('Лев')
# elif month == 'август' and 22 <= number <= 31 or month == 'сентябрь' and 1 <= number <= 23:
#   print('Дева')
# elif month == 'сентябрь' and 24 <= number <= 31 or month == 'октябрь' and 1 <= number <= 23:
#   print('Весы')
# elif month == 'октябрь' and 24 <= number <= 31 or month == 'ноябрь' and 1 <= number <= 22:
#   print('Скорпион')
# elif month == 'ноябрь' and 23 <= number <= 30 or month == 'декабрь' and 1 <= number <= 22:
#   print('Стрелец')
# elif month == 'декабрь' and 23 <= number <= 31 or month == 'январь' and 1 <= number <= 20:
#   print('Козерог')
# elif month == 'январь' and 21 <= number <= 31 or month == 'февраль' and 1 <= number <= 19:
#   print('Водолей')
# elif month == 'февраль' and 20 <= number <= 29 or month == 'март' and 1 <= number <= 20:
#   print('Рыбы')
# else:
#   print('Неправильный ввод')
