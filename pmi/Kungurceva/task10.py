#Задача 10. Вариант 7.
#апишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, 
#которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. 
#Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать 
#их туда из характеристик, которым он решил присвоить другие значения.
#Кунгурцева А.В.
#09.04.2017
balls = 30 
scores = {"Сила":"0","Здоровье":"0","Мудрость":"0","Ловкость":"0"}
punkts = 0 
choice = None 
print(
  """     Добро пожаловать в программу "Генератор персонажей"!
   Вам предоставлено 30 пунктов, которые вы можете распределить
 между следующими характеристиками: Сила, Здоровье, Мудрость, Ловкость.
  """
	)
while choice != 0 :
    print(
    """Меню

0 - Выход
1 - Добавить пункты
2 - Убрать пункты
3 - Просмотреть характеристики
""")
    choice = int(input("Выберите интересующий Вас пункт меню: "))
    if choice == 0 :
        print("\nДо свидания.")
    elif choice == 1 :
        print("Для добавления пунктов Вам доступны следующие характеристики:\n")
        for item in scores :
            print(item)
        char = str(input("\nВведите название интересующей Вас характеристики: "))
        char = char.title()
        while char not in scores :
             print("Такой характеристики нет.")
             char = str(input("\nПопробуйте ещё раз: "))
             char = char.title()
        else :
            print("\nДоступно:", balls, "пунктов.")
            punkts = int(input("\nВведите количество пунктов для добавления к выбранной характеристики: "))
            while (punkts > balls) or (punkts < 0) :  
                print("Недопустимое значение")
                punkts = int(input("\nВведите другое значение, не превышающее количество доступных пунктов: "))
        scores[char] = punkts
        print("\n", punkts, "пунктов было добавлено к '",char,"'\n")
        balls -= punkts
    elif choice == 2 :
        print("\nДля удаления пунктов Вам доступны следующий характеристики:\n ")
        for item in scores: 
            print(item)
        char = str(input("\nВведите название интересующей Вас характеристики: "))
        char = char.title()
        while char not in scores :
             print("Такой характеристики нет.")
             char = str(input("\nПопробуйте ещё раз: "))
             char = char.title()
        else :
            print("\nДоступно", scores[char], "пунктов:")
            punkts = int(input("\nВведите количество пунктов для удаления из выбранной характеристики: "))
            while (punkts > int(scores[char])) or (punkts < 0) : 
                print("Недопустимое значение.")
                punkts = int(input("\nВведите значение, не превышающее доступное количество пунктов: "))
        scores[char] = punkts
        print("\n", punkts, "пунктов было удалено из '",char,"'\n")
    elif choice == 3 :
        for item in scores :
            print(item, " = ", scores[item])
    else :
        print("\nВыбранного вами пункта нет в меню.\n")
input ("")
