#Задача 10. Вариант 1
#Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.

#Анкудинов Владимир Эдуардович
#23.04.2017

point=30
strenge=0
agility=0
healsy=0
widom=0
size=0
print("Правила распределения характеристик персонажа:"
      +"\nХарактеристика выбирается по ее названию;"
	  +"\nЕсли хотите понизить характеристику ставтье занк -, если нет, то знак не нужен")
ready="нет"
while ready != "да":
 print("\nВаши характеристики на данный момент:"
       +"\n\nСила: " + str(strenge) 
	   +"\nЛовкость: " + str(agility)
	   +"\nЗдоровье: " + str(healsy)
	   +"\nМудрость: " + str(widom)
	   +"\nОсталось очков: " + str(point))
 up=input("\nКакую характеристику вы хотите повысить: ")
 size=input("На сколько пунктов вы хотите повысить или понизить: ")
 size=int(size)
 if (abs(size) > abs(point)) or (strenge+size < 0) or (agility+size < 0) or (healsy+size < 0) or (widom+size < 0) :
   print("Вам не хаватает очков")
 else:
   if up=="Сила":
    strenge=strenge+size
    point=point-size
   elif up=="Ловкость":
    agility=agility+size
    point=point-size
   elif up=="Здоровье":
    healsy=healsy+size
    point=point-size
   elif up=="Мудрость":
    widom=widom+size
    point=point-size



 ready=input ("Завершить создание персонажа?: ")

input ("\n\nНажмите Enter, что бы выйти")