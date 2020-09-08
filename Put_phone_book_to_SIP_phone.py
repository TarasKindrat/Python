import requests
import re
import time

FILE = open('contacts')
HOST = '192.168.11.86'
FORM_URL = f"http://{HOST}/pdir.htm"
POST_URL = f"http://{HOST}/pdir.spa"

# Get user's names and phone numbers
list_users_number = [x.strip() for x in FILE]

# Get names of field where put data : "28526": "n=Name SecondName;p=909644444" where name = "28526"
response_fields_names = requests.get(FORM_URL)
list_fields_names = re.findall(r'"(\d{5})"', response_fields_names.text)
list_fields_names.sort()
# print(list_fields_names)

# Create dict for sending to request
if len(list_fields_names) >= len(list_users_number):
    data_dict = {list_fields_names[i]: list_users_number[i] for i in range(0, len(list_users_number))}

# print(data_dict)
requests_put = requests.post(POST_URL, data=data_dict)
print(f"All done {requests_put.status_code}")
time.sleep(5)


############################################################################################################################################


# headers2 = {
# "Host": "192.168.11.86",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
# "Accept-Encoding": "gzip", "deflate"
# "Content-Type": "application/x-www-form-urlencoded",
# "Content-Length": "832",
# "Origin": "http://192.168.11.86",
# "Connection": "keep-alive",
# "Referer": "http://192.168.11.86/pdir.htm",
# "Upgrade-Insecure-Requests": 1
# }
