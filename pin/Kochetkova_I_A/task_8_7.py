#-*- coding: cp1251-*-
# ������ 8 ������� 7
# �����������	����	"���������"	(��.	�.������	�������������	��	Python.	��.4) ���,	�����	�	�������	�����	����������	���������.	�����	������	��������	�����	�� ���������	�	���	������,	����	�	����	���	�������	�������������.	������������ �������	����������	�����,	��	�������	��	������,	����������	�����	���	���������, ��������	������	���,	���	��������	���������.
# Kochetkova I.A.
# 12.04.2017

import random
score=10
selection='���'
name=''
list=('�����','�����','������','�������','����������')
word=random.choice(list)
answer=word
newword=''
while word:
    first=random.randrange(len(word))
    newword+=word[first]
    word=word[:first]+word[(first+1):]
print('��������� ��������� ',newword)
while name!=answer:
    name=input('\n��� �����: ')
    if name!=answer:
        print('\n�� �������� �� ���������\n')
        selection=input('������ ������������ ���������? (��\���)\n\n')
    if selection=='��':
        score-=5
        if answer=='�����':
            print('�������� ��������')
        elif answer=='�����':
            print('������� �����, ����� �� �����')
        elif answer=='������':
            print('�� ��� ���� ���')
        elif answer=='�������':
            print('����� ���')
        elif answer=='����������':
            print('�������� �����')
        selection='���'
if name==answer:
    print('\n�� �������� ���������')
    score+=10
print('����� � ���',score,'�����')
input('\n������� ����� ��� ������')
        
