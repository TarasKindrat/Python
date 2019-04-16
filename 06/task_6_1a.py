# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


ip_address = input('Enter IP address like 10.0.1.1:  ')
ip_is_real = False
if len(ip_address.strip().split('.')) == 4:
    list_ip = ip_address.strip().split('.')
    for i in list_ip:
        if i.isdigit():
            if 0 <= int(i) <= 255:
                ip_is_real = True
            else:
                ip_is_real = False
                print(ip_address + ' Incorrect IPv4 address, must be in range 1 to 255 ')
                break
        else:
            ip_is_real = False
            print(ip_address + ' Incorrect IPv4 address, must consist only from digits!')
            break
else:
    ip_is_real = False
    print(ip_address + ' Incorrect IPv4 address, IP adres must consist from 4 octets separated - "." !')



if ip_is_real:
    print(list_ip)
    print(list_ip[0])
    if 1 <= int(list_ip[0]) <= 223 :
        print(ip_address + ' is unicast')
    elif 224 <= int(list_ip[0]) <= 239:
         print(ip_address + ' is multicast')
    elif ip_address == '255.255.255.255':
        print(ip_address + ' local broadcast')
    elif ip_address == '0.0.0.0':
        print(ip_address + ' unassigned')
    else:
        print('unused')
