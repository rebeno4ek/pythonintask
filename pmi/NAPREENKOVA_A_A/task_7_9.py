#Задача 7. Вариант 9.
#Создайте игру, в которой компьютер загадывает имя одного из трех поросят, а
#игрок должен его угадать. Разработайте систему начисления очков для задачи 6, в соответствии с которой
#игрок получал бы большее количество баллов за меньшее количество попыток.

#Napreenkova A. A.
#15.03.2017

import random
tries = 1
score = 1000
print('Я загадал одного из трёх поросят.')
pig = random.randint(1,3)
if pig == 1:
	guessed = 'Ниф-Ниф'
elif pig == 2:
	guessed = 'Наф-Наф'
elif pig == 3:
	guessed = 'Нуф-Нуф'
name = input('Угадай какого!')
while name != guessed:
	tries += 1
	score -= 300
	name = input('\n\nПопробуйте снова:')
print('\nВерно! Это', guessed, 'Вам потребовалось', tries, 'попыток')
print('\nНачислено' , score , 'очков')
input('\n\nPress Enter')

