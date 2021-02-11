import os
from os import listdir
from os.path import isfile, join
import email
from email.policy import default
import mimetypes
mypath = "E:\\mails\\new"
mypath_photo = "E:\\mails\\photo"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def extract_body(msg, depth=0):
    """ Extract content body of an email messsage
    from https://gist.github.com/ktmud/cb5e3ca0222f86f5d0575caddbd25c03
     ktmud/parse_email.py 
    """
    body = []
    if msg.is_multipart():
        main_content = None
        # multi-part emails often have both
        # a text/plain and a text/html part.
        # Use the first `text/plain` part if there is one,
        # otherwise take the first `text/*` part.
        for part in msg.get_payload():
            is_txt = part.get_content_type() == 'text/plain'
            if not main_content or is_txt:
                main_content = extract_body(part)
            if is_txt:
                break
        if main_content:
            body.extend(main_content)
    elif msg.get_content_type().startswith("text/"):
        # Get the messages
        charset = msg.get_param('charset', 'utf-8').lower()
        # update charset aliases
        charset = email.charset.ALIASES.get(charset, charset)
        msg.set_param('charset', charset)
        try:
            body.append(msg.get_content())
        except AssertionError as e:
            print('Parsing failed.    ')
            print(e)
        except LookupError:
            # set all unknown encoding to utf-8
            # then add a header to indicate this might be a spam
            msg.set_param('charset', 'utf-8')
            body.append('=== <UNKOWN ENCODING POSSIBLY SPAM> ===')
            body.append(msg.get_content())
    return body




for file in onlyfiles:
    file = join(mypath, file)
    print(file)
    with open(file, 'rb') as fp:
        msg = email.message_from_binary_file(fp, policy=default)
       # Get body of message
        body = '\n\n'.join(extract_body(msg))
        # print("subject", msg['subject'])
        # print("To", msg['To'])
        # print("From", msg['From'])
        # Print all key value pairs
        for key, value in msg.items():
            print(key, ':', value)
        print(body)
        # Extract photo in exist
        for part in msg.walk():
            print(part.get_content_type())
            # print(part.get_filename())
            if part.get_content_type() == "image/jpeg":
                filename = part.get_filename()
                print(filename)
                print(part.get('Content-Disposition'))
                print(part.get('Content-Transfer-Encoding'))
                # Write photo to separate folder
                with open(os.path.join(mypath_photo, filename), 'wb') as fp:
                  fp.write(part.get_payload(decode=True))

        print('-*-' * 30)






        # counter = 1
        # for part in msg.walk():
        #
        #     # multipart/* are just containers
        #     if part.get_content_maintype() == 'multipart':
        #         continue
        #     # Applications should really sanitize the given filename so that an
        #     # email message can't be used to overwrite important files
        #
        #     filename = part.get_filename()
        #     if not filename:
        #         ext = mimetypes.guess_extension(part.get_content_type())
        #         if not ext:
        #             # Use a generic bag-of-bits extension
        #             ext = '.bin'
        #         filename = 'part-%03d%s' % (counter, ext)
        #     counter += 1
        #     with open(os.path.join(mypath, filename), 'wb') as fp:
        #         fp.write(part.get_payload(decode=True))








    # msg = message_from_binary_file(open(filename, mode="rb"),
    #                                    policy=policy.default)
        #print(str(msg2))
    # print(FILE.read())
    # Get user's names and phone numbers
    #list_users_number = [x.strip() for x in FILE]
    #print(list_users_number)


# import mailparser
#
# # mail = mailparser.parse_from_file(email_letter)
# # print(mail)
# mail = mailparser.parse_from_string(email_letter)
# print(mail)


