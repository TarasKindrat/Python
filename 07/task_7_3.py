# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:
- считывались строки, в которых указаны MAC-адреса
- каждая строка, где есть MAC-адрес, должна обрабатываться таким образом,
  чтобы на стандартный поток вывода была выведена таблица вида:

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

is_ignored = False

from sys import argv
#file_read = str(argv)
file_read = 'CAM_table.txt'
with open(file_read) as file:
    for line in file:
        list = line.split()
        for item in list:
           if len(item.split('.')) == 3:
               print('{} {:>17} {:>9}'.format(list[0], list[1], list[3]))



