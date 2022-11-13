# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

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
                    phonehome2=random_string("phonehome2", 11), notes=random_string("notes", 6),
                    bday='"11"', bmonth='"December"', aday='"7"', amonth='"October"')
            for i in range(2)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_createcontact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

