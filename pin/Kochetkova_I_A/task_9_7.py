#-*- coding: cp1251-*-
# ������ 9 ������� 7
# ��������	����,� ������� ��������� �������� �����-���� �����,	�	����� ������ ��� ��������. ��������� �������� ������, ������� ���� � �����, � ���� ����	������� ������,	���� ��	�����-����	����� �	�����, ������ ���������	����� ��������	������ "��"	��� "���".	�����	��	���	�����	������	�����������	��������	�����.
# Kochetkova I.A.
# 12.04.2017

import random
words=('�����������','�������','�����','���������')
word=random.choice(words)
number=len(word)
print('� ������� �����, ���� ������ ��� ��������.')
print('��������� ���� � �����: '+str(number))
for i in range(5):
    k=0
    a=0
    number=len(word)
    check=word[a]
    letter=input('�������� �����: ')
    while (number>1):
        if (letter==check):
            k=k+1
            a=a+1
            check=word[a]
        else:
            a=a+1
            check=word[a]
        number=number-1
    if (letter==word[a]):
        k=k+1
    print('����� '+'"'+str(letter)+'"'+' ����������� � ����� '+str(k)+' ���')
answer=input('\n\n��� �����: ')
if (answer==word):
    print('�� ��������! ��� ��������� �����: '+str(word))
else:
    print('����, �������� ��� �� �������')
input('\n������� ����� ��� ������')