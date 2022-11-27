from model.contact import Contact
import random

def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(name="testname", middlename="testmiddlname", surname="testsurname",
                                    nickname="testnickname", title="testtitle", company="testcompany",
                                    address="testaddress", phonehome="testphonehome", phonemobile="testphonemobile",
                                    phonework="testphonework", phonefax="testphonefax", mail1="testmail1",
                                    mail2="testmail2", mail3="testmail3", hp="testhp",
                                    byear="1980", ayear="2022", address2="testaddress2",
                                    phonehome2="testhome2", notes="testnotes", bday='"11"',
                                    bmonth='"September"', aday='"10"', amonth='"October"')))
    old_contacts = db.get_contact_list()
    contact = Contact(name="Maria", middlename="Kate", surname="White",
                      nickname="mariakate", title="new_title", company="Big Company",
                      address="Moscow, Lenina 24", phonehome="89990002233", phonemobile="89991112223",
                      phonework="81112223344", phonefax="112233", mail1="mariakate@mail.com",
                      mail2="bigcompany@mail.com", mail3="work@mail.com", hp="mariakate.com",
                      byear="1989", ayear="2020", address2="Saint Petersburg",
                      phonehome2="Lomonosova 25", notes="new_notes", bday='"11"',
                      bmonth='"December"', aday='"7"', amonth='"december"')
    selection = random.choice(old_contacts)
    app.contact.edit_contact_by_id(selection.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)