# Задача 3. Вариант 11.
#Напишите программу, которая выводит имя "Анна Андреевна Горенко", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Lishutina O. A.
#15.03.2017

print("Герой нашей сегоднешней программы 'Анна Андреевна Горенко'")
a = input("Под каким фамилием вы знаете данного человека:")
if a == "Ахматова":
    print("Все верно, А.А.Горенко - А.А.Ахматова")
else:
    print("Не правильно, ты не угадал")

input("\nНажмите enter чтобы выйти.")