from model.contact import Contact


def test_edit_contact(app):
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
    app.contact.edit_first_contact(Contact(name="Jane", middlename="Lane", surname="Robert",
                               nickname="janelane", title="title", company="New Company",
                               address="Lomonosova 28", phonehome="89991112233", phonemobile="87771112233",
                               phonework="89892223311", phonefax="88984546611", mail1="janelane@mail.com",
                               mail2="newcompany@mail.com", mail3="janework@mail.com", hp="janelane.ru",
                               byear="1977", ayear="2015", address2="Moscow",
                               home2="Lenina 25", notes="otes", bday="\"9\"",
                               bmonth="\"October\"", aday="\"12\"", amonth="\"november\""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)