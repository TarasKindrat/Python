# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'OSPF    10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

list_ospf = ospf_route.strip().split()
list_ospf.remove('via')
list2_ospf = [element.strip('[').strip(']').strip(',') for element in list_ospf]
print (list2_ospf)

keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

for i in range(len(keys)):
   print('{:<20} {}'.format(keys[i],list_ospf[i]))