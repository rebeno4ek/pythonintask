# Задача 4. Вариант 13.
# Напишите программу, которая выводит имя, под которым скрывается Жан Батист Поклен.
# Дополнительно необходимо вывести область интересов указанной личности, место рождения,
# годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти).
# Для хранения всех необходимых данных требуется использовать переменные.
# После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Salov A. S.
# 14.03.2017

name = 'Мольер'
interes = 'драматург, камедеограф и актёр'
mestorozhd = 'Париже, что во Франции'
dnr = int('15')
mer = int('01')
gor = int('1622')
dns = int('17')
mes = int('02')
gos = int('1673')
age=(gos-gor)
age=int(age)
if dns<dnr and mes<=mer:
	age -= 1
elif mes<mer:
	age -= 1
print('Жан Батист Поклен, более известен как '+name)
print('Родился в '+mestorozhd)
print('Известен миру как '+interes)
print('Родился: ',dnr,mer,gor)
print('Умер: ',dns,mes,gos)
if 1<=age%10<=4:
	god='год'
else:
	god='лет'
print('Прожил ',age,god)
input()
