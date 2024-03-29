#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re
import sys




# HOST_GET = 'http://192.168.54.60:81/pdir.htm' # Phone with phonebook
# HOST_POST = '192.168.54.71:81' # Where should be written phonebook
HOST_GET = f'http://{sys.argv[1]}/pdir.htm'
HOST_POST = sys.argv[2]
ACTION = sys.argv[3]


# Actions depends phone type
# ACTION_CSC = 'pdir.csc'
# ACTION_SPA = 'pdir.spa'
FORM_URL = f"http://{HOST_POST}/pdir.htm"
POST_URL = f"http://{HOST_POST}/{ACTION}"

####################  Get list of contacts from some phone  ###########################

requests_get = requests.get(HOST_GET).text

# Get contacts from some phone
list_contacts = re.findall(r'"(n=\w.+?;p=\w.+?)"', requests_get)
print("Length of contacts", len(list_contacts))
print("Contacts:", list_contacts)


# Get names of field where put data : "28526": "n=Melnyk Igor;p=90964165589" where name = "28526"
response_fields_names = requests.get(FORM_URL).text
#print(response_fields_names)

#list_fields_names = re.findall(r'"(\d{5})"', response_fields_names)
list_fields_names = re.findall(r'name="(\d{3,5})"', response_fields_names)
list_fields_names.sort()
print("Length of list with fieleds names", len(list_fields_names))
print("Fieleds names:", list_fields_names)

data_dict = dict()
# Create dict for sending to request
if len(list_fields_names) >= len(list_contacts):
    data_dict = {list_fields_names[i]: list_contacts[i] for i in range(0, len(list_contacts))}


print("Data dict:")
print("Dictionary with data to write", data_dict)
requests_put = requests.post(POST_URL, data=data_dict)
print(f"Status {requests_put}")
print(f"Status code {requests_put.status_code}")



