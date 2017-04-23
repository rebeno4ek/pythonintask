# Задача 9. Вариант 11.
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, 
# есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". 
# Вслед за тем игрок должен попробовать отгадать слово.

# Zaytsev N.S. 
# 08.04.2017

print ('Программа случайным образом загадывает слово и сообщает количество букв в нём.')
print ('Вы должны угадать его.')
print ('\n\t\t\tП Р А В И Л А')
print ('\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
print ('Тебе даётся пять попыток узнать есть ли какая-либо буква в слове.')
print ('Программа тебе сообщит, есть ли введённая тобой буква слове или её нет.')
print ('\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
print ('\t\t\tУдачной игры!')

import random
WORD = None #выбранное программой слово

def choose_word(): #функция выбора (загадывания) слова программой
    global WORD

    words_files = open('words.txt', 'r') #открыть файл для чтения всех слов
    words = list() #массив всех слов из файла
    for line in words_files:
        words.append(line.strip()) #заполнить массив всеми словами из файла, strip применить для отбрасывания лишних символов, здесь таковым является символ \n - перенос
    
    WORD = words[random.randint(0, len(words) - 1)] #выбрать(загадать) случайное слово


def game():
    global WORD

    choose_word() #загадать слово
    print('\nЯ загадал слово, в нем {0} букв.'.format(len(WORD)))
    print('\nТеперь можешь спрашивать о буквах в слове.')
    for i in range(5):
        letter = input('Есть ли в слове буква: ') 
        if len(letter) == 1 and (letter.lower() >= 'а' and letter.lower() <= 'я' or letter.lower() == 'ё'): #если введен 1 символ, и он - буква
            if letter.lower() in WORD: 
                print('Да! Такая буква есть.') 
            else:
                print('Увы, но такой буквы нет.')
        else:
            print('Это не буква!')

    user_word = input('Попробуй отгадать слово: ') 
    if user_word.lower() == WORD: 
        print('Вау! Ты угадал слово и выиграл!')
    else:
        print('Неверно! Я загадал слово: {0}.'.format(WORD)) 

    user_answer = input('Сыграем еще раз? (да/нет) ') 
    #метод strip() удаляет пробелы по краям
    if user_answer.strip().lower() == 'да': 
        game() #запустить игру заново


if __name__ == '__main__':
    game()
input ('Press ENTER to exit from programm...')