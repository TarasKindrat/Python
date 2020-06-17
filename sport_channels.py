import requests
import json
import xml.etree.ElementTree as xml
from datetime import datetime, timedelta

TIME_OFFSET = '0000'
NEXT_DAYS = 3
COUNTRY_CODE = 'ZA'
SAVE_FILE_DIRECTORY_AND_NAME = 'EPG.xml'

START_TIME = str(datetime.now().timestamp()).split('.')[0]
NEXT_N_DAYS_TIME = str((datetime.now() + timedelta(days=NEXT_DAYS)).timestamp()).split('.')[0]

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/79.0.3945.88 Safari/537.36'
HEADER_REFER = 'https://supersport.com/tv-guide'
REQUEST_REEFER = 'https://s'
# Create header for request, without header answer will be : 404
HEADER = {'accept': 'application/json', 'accept-encoding': 'gzip, deflate, br', 'referer': HEADER_REFER,
          'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': USER_AGENT,
          'x-requested-with': 'XMLHttpRequest'}


def convert_time(time_from_dictionary):
    """
     Get time like:
    :param time_from_dictionary: "2020-01-13T07:00:00Z"
    :return: "20200113070000"
    """
    return time_from_dictionary[0:4] + time_from_dictionary[5:7] + time_from_dictionary[8:10] + \
           time_from_dictionary[11:13] + time_from_dictionary[14:16] + time_from_dictionary[17:19]


def createXML(list_text):
    """
    Create XML file.
    :param list_text:
    :return: nothing only create XML
    """
    root = xml.Element('tv')
    root.set('generator', 'python')
    for dict in list_text:
        channel = xml.Element('channel')
        channel.set('id', str(dict['channel']))
        name = xml.SubElement(channel, 'display-name')
        name.text = str(dict['channel'])
        root.append(channel)

        programme = xml.Element('programme')
        programme.set('start', convert_time(dict['starts_at'])+' +' + TIME_OFFSET)
        programme.set('stop', convert_time(dict['ends_at'])+' +' + TIME_OFFSET)
        programme.set('channel', str(dict['channel']))
        title = xml.SubElement(programme, 'title')
        title.set('lang','en')
        title.text = '"'+str(dict['title'])+'"'
        root.append(programme)

    tree = xml.ElementTree(root)

    epg_file = SAVE_FILE_DIRECTORY_AND_NAME

    #write to XML file
    try:
        with open(epg_file, "wb") as fh:
            tree.write(fh)
    except Exception:
        print("Some error to write XML: " + Exception)
        exit(1)

# Make request
try:
    response = requests.get(REQUEST_REEFER + '?timestamps[]=' + START_TIME + '&timestamps[]=' +
                            NEXT_N_DAYS_TIME + '&live=false&country_code=' + COUNTRY_CODE, headers=HEADER)
    # IF responce 404
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
	    print('ERROR: %s' %e)

# Other exeptions
except Exception:
    print("Some error occured, check url or internet connection  or some other, error is: " + Exception)
    exit(1)

# Convert to list of dictionary
list_text = json.loads(response.text)
createXML(list_text)
