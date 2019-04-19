# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
is_ignored = False
from sys import argv
file_read = argv[1]
file_write = open('config_sw1_cleared.txt','a')
#file_read = 'config_sw1.txt'
with open(file_read) as file:
    for line in file:
        for ignored in ignore:
            if ignored in line:
                is_ignored = True
                break
            else:
                is_ignored = False

        if not is_ignored:
            print(line.strip('\n'))
            file_write.write(line)

file_write.close()