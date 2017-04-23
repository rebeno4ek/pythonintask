#Задача 10. Вариант 18.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, 
#которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. 
#Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать 
#их туда из характеристик, которым он решил присвоить другие значения.

#Shamugija L.G.
#13.03.2017

run = 30 
person = {"Сила":"0","Здоровье":"0","Мудрость":"0","Ловкость":"0"}
points = 0 
choice = None 
print(
  """	            Добро пожаловать!
            Вы запустили "Генератор персонажей"
          Вам предоставлено 30 пунктов, которые вы 
        можете распределить между 4 характеристиками.
  """
	)
while choice != 0 :
    print(
    """Меню

	0 - Выход
	1 - Просмотр характеристик
	2 - Добавить пункты к характеристике
	3 - Уменьшить пункты характеристики
    """
    )
    choice = int(input("Что вы хотите сделать? Выберите соответствующий пункт меню: "))
    if choice == 1 :
        print("\nХарактеристики героя:\n")
        for item in person :
            if (item == "Ловкость") or (item == "Мудрость") or (item == "Здоровье") :
              print(item, " | ", person[item])
            else :
              print(item, "\t  | ", person[item])
    elif choice == 2 :
        print("Пожалуйста, введите характеристику, в которую хотите добавить пунктов. \nДля изменения доступны", len(person), "характеристики:\n")
        for item in person :
            print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person :
             print("Такой характеристики нет. Пожалуйста, проверьте введенные данные: ")
             char = str(input("\n:"))
             char = char.title()
        else :
            print("\nВведите количество пунктов для этой характеристики. У вас есть", run, "свободных пунктов")
            points = int(input("\n:"))
            while (points > run) or (points < 0) :  
                print("Вы не можете назначить такое количество пунктов. \nВам доступно", run, "свободных пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было добавлено к", char)
        run -= points 
    elif choice == 3 :
        print("Пожалуйста, введите имя характеристики для снятия пунктов.", "Доступно изменение для: ")
        for item in person:
            if int(person[item]) > 0 : 
                print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person :
             print("Такой характеристики нет. Пожалуйста, проверьте введенные данные: ")
             char = str(input("\n:"))
             char = char.title()
        else :
            print("\nВведите количество пунктов для характеристики. Доступно", person[char], "пунктов:")
            points = int(input("\n:"))
            while (points > int(person[char])) or (points < 0) : 
                print("Невозможно удалить такое количество пунктов. Доступно", person[char], "пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было удалено")
        ochki += points
    elif choice == 0 :
        print("Пока!")
    else :
        print("Выбранного вами пункта нет в меню")
