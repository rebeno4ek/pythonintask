# Задача 8.
# Bogodarov A.A
# 2017-04-03
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
# подсказку в том случае, если у него нет никаких предположений. Разработайте
# систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
# получали больше тех, кто запросил подсказку

# Анаrраммы 


import random

WORDS=(("хоккей", "шайба"), ("клюшка", "инвентарь"), ("счет", "результаты игры"), ("кошка", "животное"), ("еда", "предмет для выживанияя"), ("раковина", "средство ддля мытья чего-либо"))
# возьмём случайное слово из набора
word = random.choice(WORDS)
advice = word[1]
word = word[0]
correct = word
jumble = ""

# запомнить исп. подсказки
adviced=0

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print(
"""
Добро пожаловать в игру 'Анаграммы'!
Вам нужно переставить буквы, чтобы получить исходную версию слова.
(Для выхода нажмите Enter. не вводя своей версии.)
"""
)
print(" Анаграмма: " + jumble)

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct or guess == "":
    if guess != "":
        print("Неверно.")
    else:
        print("Подсказка: " + advice)
        adviced = 1

    guess = input("Попробуйте отгадать исходное слово: ")

if guess == correct:
    print("Дa. именно так! Вы отгадали!\n")
    if adviced:
        print("Вы использовали подсказку и заработали 1 балл")
    else:
        print("Вы не использовали подсказку и заработали 2 балла")

print("Cnacибo за игру.")
input("\n\nHaжмитe Enter. чтобы выйти.")