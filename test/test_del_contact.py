from model.contact import Contact
import random

def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(name="testname", middlename="testmiddlname", surname="testsurname",
                               nickname="testnickname", title="testtitle", company="testcompany",
                               address="testaddress", phonehome="testphonehome", phonemobile="testphonemobile",
                               phonework="testphonework", phonefax="testphonefax", mail1="testmail1",
                               mail2="testmail2", mail3="testmail3", hp="testhp",
                               byear="1980", ayear="2022", address2="testaddress2",
                               phonehome2="testhome2", notes="testnotes", bday="\"11\"",
                               bmonth="\"September\"", aday="\"10\"", amonth="\"October\"")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)