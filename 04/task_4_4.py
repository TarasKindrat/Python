# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
number1 = command1.find('1')
slis_e1 = command1[number1:] # get vlans

list1 = []

list1 = (slis_e1.strip().split(','))
print(list1)
#####################################################
number2 = command2.find('1')
slis_e2 = command2[number2:]
set1 = set(list1)

list2 = []

list2 = (slis_e2.strip().split(','))
list1.sort()
list2.sort()
print(list2)
set2 = set(list2)
set3 = set2.intersection(set1)
print(set3)
