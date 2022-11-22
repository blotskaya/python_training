from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(name=random_string("name", 10), middlename=random_string("middlename", 8),
                    surname=random_string("surname", 10), nickname=random_string("nickname", 7),
                    title=random_string("title", 11), company=random_string("company", 12),
                    address=random_string("address", 20), phonehome=random_string("phonehome", 9),
                    phonemobile=random_string("phonemobile", 10), phonework=random_string("phonework", 6),
                    phonefax=random_string("phonefax", 12), mail1=random_string("mail1", 20),
                    mail2=random_string("mail2", 11), mail3=random_string("mail3", 15), hp=random_string("hp", 10),
                    byear="1989", ayear="2020", address2=random_string("address2", 12),
                    phonehome2=random_string("phonehome2", 11), notes=random_string("notes", 6))
            for i in range(2)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))