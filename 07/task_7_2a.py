# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
is_ignored = False

from sys import argv
#file_read = str(argv)
file_read = 'config_sw1.txt'
with open(file_read) as file:
    for line in file:
        if '!' in line[0:]:
            continue
        else:
            for ignored in ignore:
                if ignored in line:
                    is_ignored = True
                    break
                else:
                    lis_ignored = False
        if not is_ignored:
            print(line.strip('\n'))


