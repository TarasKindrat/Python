# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

ignore = ['duplex', 'alias', 'Current configuration']
is_ignored = False
from sys import argv
file_read = argv[1]
file_write = open(argv[2],'a')
#file_write = open('config_sw1_cleared.txt','a')
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
