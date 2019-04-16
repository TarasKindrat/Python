# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_address = input('Enter IP address like 10.0.1.1:  ')
list_ip = ip_address.split('.')
print(list_ip)
print(list_ip[0])
if 1 <= int(list_ip[0]) <= 223 :  #and list_ip[0].isdigit() >= 1:
    print(ip_address + ' is unicast')
elif 224 <= int(list_ip[0]) <= 239:
    print(ip_address + ' is multicast')
elif ip_address == '255.255.255.255':
    print(ip_address + ' local broadcast')
elif ip_address == '0.0.0.0':
    print(ip_address + ' unassigned')
else:
    print('unused')
