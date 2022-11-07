from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(name="testname", middlename="testmiddlname", surname="testsurname",
                               nickname="testnickname", title="testtitle", company="testcompany",
                               address="testaddress", phonehome="testphonehome", phonemobile="testphonemobile",
                               phonework="testphonework", phonefax="testphonefax", mail1="testmail1",
                               mail2="testmail2", mail3="testmail3", hp="testhp",
                               byear="1980", ayear="2022", address2="testaddress2",
                               home2="testhome2", notes="testnotes", bday="\"11\"",
                               bmonth="\"September\"", aday="\"10\"", amonth="\"October\"")))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="Maria", middlename="Kate", surname="White",
                      nickname="mariakate", title="new_title", company="Big Company",
                      address="Moscow, Lenina 24", phonehome="Lenina 24", phonemobile="89991112223",
                      phonework="Big Company", phonefax="112233", mail1="mariakate@mail.com",
                      mail2="bigcompany@mail.com", mail3="work@mail.com", hp="mariakate.com",
                      byear="1989", ayear="2020", address2="Saint Petersburg",
                      home2="Lomonosova 25", notes="new_notes", bday="\"11\"",
                      bmonth="\"December\"", aday="\"7\"", amonth="\"October\"")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)