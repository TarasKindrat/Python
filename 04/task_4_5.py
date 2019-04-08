# -*- coding: utf-8 -*-
'''
Задание 4.5

Список VLANS это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLANS.sort()
set1 = set(VLANS)  # make unique
print(set1)
string1 = str(set1).strip('{').strip('}')
print(string1)

list1 = string1.split(', ')

list2 = [int(vlan) for vlan in list1 if vlan.isdigit()]  # convert to int
list2.sort()
rint(list2)
