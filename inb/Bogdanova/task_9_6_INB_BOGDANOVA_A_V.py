# Задача 9. Вариант 6.

#Создайте игру, в которой компьютер какое-либо выбирает слово, а игрок должен его отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет".
#Вслед за тем игрок должен попробовать отгадать слово.

#Bogdanova A. V.

import random

words = ("весна" , "тюльпаны" , "море" , "снимки" , "настроение" , "наушники")
word = random.choice(words)

# Начало игры

print(
     """
        Добро пожаловать в игру "Отгадай слово"
        Надо отгадать слово при этом вы можете 5 раз спросить у компьютера если там какие-либо буквы
    (Для выхода нажмите enter, не вводя своей версии)
                   """
)

print ("\nДлина слова составляет:", len(word), "букв(ы)")
print ("Итак, мы начинаем, у вас есть 5 попыток, чтобы отгадать слово.")

for tries in range(4):
      letter=input("Ваше предположение: ")
      if letter in word:
         print("Да")
      else:
         print("Нет")

guess=input("Попробуйте угадать: ")
if guess == word:
    print("Поздравляю, вы отгадали!")
else:
    print("К сожалению, вы использовали все попытки.")
    print("Это было слово" , word)
print("Игра окончена! До новых встреч!")
input("\nНажмите Enter, чтобы выйти.")
