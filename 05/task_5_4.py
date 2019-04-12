# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

index = 0
index2 = 0


number = input('Enter word from numbe_list ')


for i in range(0,len(num_list)):
    if str(num_list[i]) == number:
        index = i
        print(index, end=',')

print(' \n last index :' + str(index))


number = input('Enter word from word_list ')
for i in range(len(word_list)):
    if str(word_list[i]) == number:
        index2 = i
        print(index2, end=',')

print(' \n last index :' + str(index2))