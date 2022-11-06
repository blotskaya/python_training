# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_createcontact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Maria", middlename="Kate", surname="White",
                               nickname="mariakate", title="new_title", company="Big Company",
                               address="Moscow, Lenina 24", phonehome="Lenina 24", phonemobile="89991112223",
                               phonework="Big Company", phonefax="112233", mail1="mariakate@mail.com",
                               mail2="bigcompany@mail.com", mail3="work@mail.com", hp="mariakate.com",
                               byear="1989", ayear="2020", address2="Saint Petersburg",
                               home2="Lomonosova 25", notes="new_notes", bday="\"11\"",
                               bmonth="\"December\"", aday="\"7\"", amonth="\"October\"")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

