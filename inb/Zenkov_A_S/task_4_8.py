# Задача 4. Вариант 8.
# Напишите программу, которая выводит имя, под которым скрывается Алексей Максимович Пешков.
# Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти).
# Для хранения всех необходимых данных требуется использовать переменные.
# После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Zenkov A.S. 
# 13.03.2017

Name = "Максим Горький"
print ("Алексей Максимович Пешков более известен, как", Name)
Interests = "писатель, прозаик, драматург."
print ("\nОбласть интересов: ", Interests)
Born = "Нижний Новгород, Российская империя."
print ("\nМесто рождения: ", Born)
Date = ("1868")
Date = int(Date)
print ("\nГод рождения: ", Date)
Death = ("1936")
Death = int(Death)
print ("\nГод смерти: ", Death, "\n")
Age = (Death - Date)
print (Name, " умер в возрасте ", Age, " лет.")
input ("\n\nНажмите Enter для выхода...")
