
# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
IP = str(argv[1:])

IP.strip().strip('.')
list_ip = IP.split('.')
last_octet_cidr = list_ip[3:]                                                    # get last octet whis cidr
list_last_octet_cidr = (str(last_octet_cidr)).strip('[]').strip("'").split('/')  # split to octet and cidr
#print(IP)
#print(list_ip)
#print(last_octet_cidr)
#print(list_last_octet_cidr)
list_ip.pop(-1)                             # delete last octet whis cidr from list
list_ip.append('0')     # add only last octet
#print(list_ip)
ip_template = '''
     IP network:
     {0:<8} {1:<8} {2:<8} {3:<8}
     {0:08b} {1:08b} {2:08b} {3:08b}
     '''
mask_template = '''
     Mask:
     /{0:<8} 
     {1:<8} {2:<8} {3:<8} {4:<8}
     {1:08b} {2:08b} {3:08b} {4:08b}
     '''
# calculate number of '1' and '0' in octets
number_of_mask = int(list_last_octet_cidr[1])

zeros = 32 - number_of_mask
zero_octet = zeros // 8
not_ful_zeros = zeros%8

one_octets = number_of_mask//8
not_full_one = number_of_mask%8

mask = ''
# fill string whis '1' and '0' like mask in binary
for i in range(one_octets):
    octet =''
    octet='1'*8
    mask = mask+octet+' '

mask_0 =''
for j in range(zero_octet ):
    octet = ''
    octet = '0' * 8
    mask_0 = mask_0 + octet + ' '


mask = mask + '1'* not_full_one + '0'*not_ful_zeros + ' '+ mask_0

list_mask = mask.strip().split()

print(ip_template.format(int(list_ip[0]), int(list_ip[1]), int(list_ip[2]), int(list_ip[3])))
print(mask_template.format(number_of_mask, int(list_mask[0],2), int(list_mask[1],2), int(list_mask[2],2), int(list_mask[3],2)))