# coding: utf-8

#������ 10. ������� 15

#�������� ��������� "��������� ����������" ��� ����. 
#������������ ������ ���� ������������� 30 �������, 
#������� ����� ������������ ����� �������� ����������������: 
#����, ��������, �������� � ��������. ���� ������� ���, 
#����� ������������ ��� �� ������ ����� ��� ������ �� ������ 
#"����", �� � ���������� �� ���� �� �������������, ������� �� 
#����� ��������� ������ ��������.

#�������� �.�
#28.02.2017

balance=30
characteristics_point=[0,0,0,0]
characteristics_list=["Power","health","Wisdom","Agility"]

print("                  Hello, you are greeted by a character generator")

command="None"
while command!="0":
        command=0
        command=input("""
1-Add point characteristics
2-delete point characteristics
3-view characteristics
0-exit
""")

        if (command=="1"):
            add_point=int(input("Type number point: "))
            balance-=add_point
            if (balance>=0):
                num_list=int(input("""
            Enter characteristics
            1-power
            2-health
            3-Wisdom
            4-Agility
             """))
                num_list-=1

                characteristics_point[num_list]+=add_point
            else:
                if balance>0:
                    print("You do not have as many points.\nYou left: ",balance)
                else:
                    print("You do not have as many points.\nYou left: 0")

        elif (command=="2"):
            delete_point=int(input("Enter delete point: "))
            balance+=delete_point
            num_list=int(input("""
    Enter characteristics
    1-power
    2-health
    3-Wisdom
    4-Agility
    """))
            num_list-=1

            characteristics_point[num_list]-=delete_point

        elif (command=="3"):
            for i in range(4):
                 print(characteristics_list[i],": ",characteristics_point[i])
        else:
            input("Thank you. Goodbye")




    

