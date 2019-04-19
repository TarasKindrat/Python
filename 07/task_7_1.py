# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt') as file:
    for line in file:
        ospf_route = line


        list_ospf = ospf_route.strip().strip(',').split()
        list_ospf.remove('via')
        list2_ospf = [element.strip('[').strip(']') for element in list_ospf]
        print (list2_ospf)

        keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

        for i in range(len(keys)):
           print('{:<20} {}'.format(keys[i],list_ospf[i].strip(',')))
