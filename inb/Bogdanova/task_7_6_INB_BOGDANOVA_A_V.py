#Задача 7. Вариант 6.

#Создайте игру, в которой компьютер загадывает название одного из семи городов России, имеющих действующий метрополитен, а игрок должен его угадать.
#Систему начисления очков для Разработайте задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

#Bogdanova A. V.

import random
tries = 1
score = 8000
name=input("\n\nНазовите один из городов, в котором есть действующее метро: ")
city=random.randint(1,7)
if city == 1:
    right = "Москва"
elif city == 2:
    right = "Санкт-Петербург"
elif city == 3:
    right = "Казань"
elif city == 4:
    right = "Екатеринбург"
elif city == 5:
    right = "Самара"
elif city == 6:
    right = "Нижний Новгород"
elif city == 7:
    right = "Новосибирск"
while name != right:
    tries += 1
    score -= 1000
    name = input("К сожалению, вы не отгадали. Попробуйте еще раз: ")
print ("И это правильный ответ! В прекрасном городе" , right, "есть действующее метро.")
print ("Вы угадали с" ,tries, "попытки.")
print ("Поздравляю, вы выиграли" , score , "баллов!")
input("\nНажмите Enter, чтобы выйти.")
