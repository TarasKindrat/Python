import requests
import re
import time

FILE = open('contacts')
HOST = '192.168.54.86'
FORM_URL = f"http://{HOST}/pdir.htm"
POST_URL = f"http://{HOST}/pdir.spa"

# Get user's names and phone numbers
list_users_number = [x.strip() for x in FILE]

# Get names of field where put data : "28526": "n=Melnyk Bogdan;p=90964167189" where name = "28526"
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
# "Host": "192.168.54.86",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
# "Accept-Encoding": "gzip", "deflate"
# "Content-Type": "application/x-www-form-urlencoded",
# "Content-Length": "832",
# "Origin": "http://192.168.54.86",
# "Connection": "keep-alive",
# "Referer": "http://192.168.54.86/pdir.htm",
# "Upgrade-Insecure-Requests": 1
# }

# data2 = "28398=n%3DKurgan+Ira%3Bp%3D90685433682&28334=&28526=n%3DAbrat+Vova%3Bp%3D90979241286&28462=&28654=n%3DKovelskij%3Bp%3D90990695617&28590=&27758=&27694=&27886=&27822=&28014=&27950=&28142=n%3DKravchenko+Dmytro%3Bp%3D90673447001&28078=&21102=&21038=&21230=&21166=&21358=&21294=&21486=&21422=&20590=&20526=&20718=&20654=&20846=&20782=&20974=&20910=&22126=&22062=&22254=&22190=&22382=&22318=&22510=&22446=&21614=&21550=&21742=&21678=&21870=&21806=&21998=&21934=&23150=&23086=&23278=&23214=&23406=&23342=&23534=&23470=&22638=&22574=&22766=&22702=&22894=&22830=&23022=&22958=&24174=&24110=&24302=&24238=&24430=&24366=&24558=&24494=&23662=&23598=&23790=&23726=&23918=&23854=&24046=&23982=&17006=&16942=&17134=&17070=&17262=&17198=&17390=&17326=&16494=&16430=&16622=&16558=&16750=&16686=&16878=&16814=&18030=&17966=&18158=&18094=&18286=&18222="
#
#
# data3 = {
#                 "28398": "n=Kurgan Oleg;p=90673441152",
#
#                 "28334": "",
#
#                 "28526": "n=Melnyk Bogdan;p=90964167189",
#
#                 "28462": ""
#               }