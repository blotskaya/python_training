from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
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
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts