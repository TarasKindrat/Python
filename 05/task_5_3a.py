# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: '

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

# macke Dictionary frol lists
interfaces = {'access': access_template, 'trunk': trunk_template}
vlan_dict = {'access': 'Enter VLAN number:', 'trunk': 'Enter allowed VLANs:'}

interface = input('Enter interface mode (access/trunk): ')
interface_type_number = input('Enter interface type and number: ')
vlans = input(vlan_dict[interface])

print('\n' + '*' * 50)
print('interface {}'.format(interface_type_number))
print('\n'.join(interfaces[interface]).format(vlans))
