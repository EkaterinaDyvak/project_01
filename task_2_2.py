# -*- coding: utf-8 -*-
"""task 2.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gJ9qj2XKDol6oSw6Em2TnGI7jikUJvSp

Задача 2.2
"""

calendar = [
    ['январь', 31], ['февраль', 28], ['март', 31], ['апрель', 30], ['май', 31],
    ['июнь', 30], ['июль', 31], ['август', 31], ['сентябрь', 30], ['октябрь', 31],
    ['ноябрь', 30], ['декабрь', 31]
    ]
kvartel=['первого', 'второго', 'третьего', 'четвертого']
mounth=int(input(' Введите номер месяца:'))
def katya(calendar):
    k=-1
    if (mounth)<=2 or (mounth)==12:
        k+=1
    elif 3<= (mounth) <=5:
        k+=2
    elif 6<= (mounth) <=8:
        k+=3
    elif 9<= (mounth) <=11:
        k+=4
    return k
print(f'месяц {mounth}({calendar[mounth-1][0]})является частью {kvartel[katya(calendar)]} квартала')