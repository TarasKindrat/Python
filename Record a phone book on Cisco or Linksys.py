import requests
import re
import time
from bs4 import BeautifulSoup
import json

FILE_WRITE = open('contacts_write2.txt', 'w')

HOST_GET = 'http://192.168.54.60:81/pdir.htm'
HOST_POST = '192.168.54.60:81'
# Actions depends phone type
ACTION_CSC = 'pdir.csc'
ACTION_SPA = 'pdir.spa'
FORM_URL = f"http://{HOST_POST}/pdir.htm"
POST_URL = f"http://{HOST_POST}/{ACTION_CSC}"

####################  PART 1  get list of contacts from some phone and write to file   ###########################

requests_get = requests.get(HOST_GET).text

# Get contacts from some phone
list_contacts = re.findall(r'"(n=\w.+?;p=\w.+?)"', requests_get)
# print(len(list_contacts))
# print(list_contacts)
# Write to file
FILE_WRITE.write('\n'.join(list_contacts))
FILE_WRITE.close()


###################  PART 2 get list pf contacts from file and write to phone   ##################################

FILE = open('contacts_write2.txt')
# print(FILE.read())
# Get user's names and phone numbers
list_users_number = [x.strip() for x in FILE]
FILE.close()


# Get names of field where put data : "28526": "n=Melnyk Igor;p=90964165589" where name = "28526"
response_fields_names = requests.get(FORM_URL).text

list_fields_names = re.findall(r'"(\d{5})"', response_fields_names)
list_fields_names.sort()
print(len(list_fields_names))
print(list_fields_names)

# Create dict for sending to request
if len(list_fields_names) >= len(list_users_number):
    data_dict = {list_fields_names[i]: list_users_number[i] for i in range(0, len(list_users_number))}

# print(data_dict)
requests_put = requests.post(POST_URL, data=data_dict)
print(f"All done {requests_put.status_code}")
#time.sleep(5)


