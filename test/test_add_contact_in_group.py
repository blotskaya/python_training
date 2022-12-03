from model.contact import Contact
import random

def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(name="testname", middlename="testmiddlname", surname="testsurname",
                                    nickname="testnickname", title="testtitle", company="testcompany",
                                    address="testaddress", phonehome="testphonehome", phonemobile="testphonemobile",
                                    phonework="testphonework", phonefax="testphonefax", mail1="testmail1",
                                    mail2="testmail2", mail3="testmail3", hp="testhp",
                                    byear="1980", ayear="2022", address2="testaddress2",
                                    phonehome2="testhome2", notes="testnotes", bday='"11"',
                                    bmonth='"September"', aday='"10"', amonth='"October"')))
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    selection_group = random.choice(old_groups)
    selection_contact = random.choice(old_contacts)
    app.contact.add_contact_in_group(selection_contact.id, selection_group.id)
