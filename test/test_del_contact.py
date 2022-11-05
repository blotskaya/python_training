from model.contact import Contact

def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create((Contact(name="testname", middlename="testmiddlname", surname="testsurname",
                               nickname="testnickname", title="testtitle", company="testcompany",
                               address="testaddress", phonehome="testphonehome", phonemobile="testphonemobile",
                               phonework="testphonework", phonefax="testphonefax", mail1="testmail1",
                               mail2="testmail2", mail3="testmail3", hp="testhp",
                               byear="1980", ayear="2022", address2="testaddress2",
                               home2="testhome2", notes="testnotes", bday="\"11\"",
                               bmonth="\"September\"", aday="\"10\"", amonth="\"October\"")))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts