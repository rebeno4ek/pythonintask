﻿# Задача 6. Вариант 8.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток
# угадать.

# Lubnin A.V.
# 04.04.2017

import random
xp = 1570
secret = random.choice(["Боровицкий холм", "Псковская горка", "Таганский холм", "Ивановская горка", "Красный холм", "Старо-Ваганьковский холм", "Чертольский холм"])
print("Программа случайным образом загадывает название одного из семи холмов Москвы. Вам необходимо отгадать какой из холмов загадан.")
while 0<1:
	luck = input("Ваше предположение: ")
	if secret.upper() == luck.upper():
		print("Вы угадали! Это был ", secret, ". Получено очков: ", int(xp))
		break
	elif xp<202:
		print("Попытки закончились, очки не начислены!")
		break
	else:		
		print("Вы не угадали! Попробуйте еще разок")
		xp*=.71
		
input("\n\n Нажмите Enter для выхода")
