###*** Very simple address book with wrtiting information to file ***###

import pickle
# Class for like objeckt for person attributes
class PersonCard:
    def __init__(self, secondname, phone, emailaddress):
        self.__secondname = secondname
        self.__phone = phone
        self.__emailaddress = emailaddress
# Define str method to return strings of propertys
    def __str__(self):
        return "\t Secondname: {}      Phone: {}      Emmail: {}".format(self.__secondname, self.__phone, self.__emailaddress)

# Create empty dictionary
addresBook = {}

# Function to get contact information from binary file to dictionary
def getAddresFromFile ():
    addresInFile = "addresBook.data"
    with open(addresInFile, 'rb') as fr:
        try:
            while True:
                addresBook.update(pickle.load(fr))
        except EOFError:
            pass
    fr.close()
    return addresBook
# Function to write contact information from to dictionary to binary file
def writeAddressToFile ():
    addresInFile = "addresBook.data"
    with open(addresInFile, 'ba+') as fp:
        pickle.dump(addresBook, fp)
    fp.close()

# function to add new person
def addContact (name, secondname, phone, emailaddress):
    addresBook.update({name : PersonCard(secondname, phone, emailaddress)})
    writeAddressToFile()

# For work with new contact
def newContacs ():
    # For endless loop
    running = True
    while running:
        data = input('Input name, secondname, phone, emaiaddress  or "stop"  to exit \n')
        # Chek line, must to be not empty
        if not len(data.strip()) == 0:
            list = data.strip().split()
            if list[0] == 'stop':
                running = False
                addresBook = getAddresFromFile()
                print("At contackt book are:")
                for key, value in addresBook.items():
                    print(str(key), '\t', str(value))
            elif len(list) == 4:
                addContact(list[0], list[1], list[2], list[3])
            else:
                print("Empty or overfull entry, please retry \n")
        else:
            print("You are entered empty line, please retry \n")
# Search contact by name
def findContact (name):
    addresBook = getAddresFromFile()
    print(addresBook.get(name, "There is no this contact at the book \n"))

# For endless main loop
running = True
while running:
    enter = input("Enter what are you want to do: \n"
                  "1   - add new contact \n"
                  "2   - find in contacts \n"
                  "3   - exit \n")
    if enter == '1':
        newContacs()
    elif enter == '2':
        nameContact = input("Enter name \n")
        findContact(nameContact)
    elif enter == '3':
        running = False
    else:
        print("Wrong enter, please reapid again! \n")
else:print("End of programm, by ...")
