# Задача 7. Вариант 16.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
# Udovenko A. Y.
# 14.03.2017
import random
print ( """
\n\t\t\t\a Добро пожаловать в игру "Угадай-ка"!
Отгадайте, какую из жен Ивана (Грозного) IV мы загадали.
        """)
number = random.randint(1, 6)
wives = ('Анастасия Романовна',
        'Марфа Собакина',
        'Анна Васильчикова',
        'Мария Нагая',
        'Мария Темрюковна',
        'Анна Колтовская')
computers_coice = wives[number]
total = 7000

human=input('Введите предполагаемое имя: ')
while human != computers_coice:
    print ('\nНеверно. Попытайтесь еще раз.')
    total -=1000
    human=input('Введите предполагаемое имя: ')

print ('Вы угадали!',computers_coice, '- вот кого мы загадали!\nВы получили', total, 'очков.\n' )


input ('Нажмите Enter, чтобы выйти.')
