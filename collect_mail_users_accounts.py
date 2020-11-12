#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

FILE_READ = open('mail_users_accounts.txt')
FILE_IMAP = open('/var/log/dovecot/info.log')

# Get mail addresses from file
list_mails_from_file = [x.strip() for x in FILE_READ]

# Convert to set
set_mails_from_file = set(list_mails_from_file)
FILE_READ.close()

# Get string text from Dovecot logs
logs = FILE_IMAP.read()
# print(len(set_mails_from_file))
# print(set_mails_from_file)

# Find mail addresses and add in list
list_logs_mails = re.findall(r'Login: user=<(\w.+?@some_domen.if.ua)>', logs)
# print(len(list_logs_mails))

# Convert to set
set_logs_mails = set(list_logs_mails)
# print(len(set_logs_mails))
# for item in set_logs_mails:
#     print(item)

# Union two sets in one
set_total_mails = set_mails_from_file.union(set_logs_mails)

FILE_WRITE = open('mail_users_accounts.txt', 'w')
FILE_WRITE.write('\n'.join(set_total_mails))
FILE_WRITE.close()

