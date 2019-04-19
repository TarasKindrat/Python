# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
sort_dict = {}
vlan_list = []
new_list = []
sort_vlans = []
set_vlans = set()

from sys import argv
#file_read = str(argv)

file_read = 'CAM_table.txt'
with open(file_read) as file:
    for line in file:
        list = line.split()
        for item in list:
           if len(item.split('.')) == 3:
               print('{} {:>17} {:>9}'.format(list[0], list[1], list[3]))
               vlan_list.append(list[0])
               new_list.append(list[0] +'   '+ list[1] +'   '+ list[3])

# make set from list of vlans it deleta the same vlans
set_vlans = set(vlan_list)
# male new list whis unrepeatable vlans and sort it
sort_vlans = [vlan_item for vlan_item in set_vlans]
sort_vlans.sort()
print(sort_vlans)
print('sorted items')
for vlan in sort_vlans:
    for item in new_list:
        if vlan in item[0:4]:
            print(item)




