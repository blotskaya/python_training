from model.contact import Contact
import random
from fixture.orm import ORMFixture
from model.group import Group

database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(name="testname", middlename="testmiddlname", surname="testsurname",
                                    nickname="testnickname", title="testtitle", company="testcompany",
                                    address="testaddress", phonehome="testphonehome", phonemobile="testphonemobile",
                                    phonework="testphonework", phonefax="testphonefax", mail1="testmail1",
                                    mail2="testmail2", mail3="testmail3", hp="testhp",
                                    byear="1980", ayear="2022", address2="testaddress2",
                                    phonehome2="testhome2", notes="testnotes", bday='"11"',
                                    bmonth='"September"', aday='"10"', amonth='"October"')))
    if len(db.get_group_list()) == 0:
        app.group.create((Group(name="testname", header="testheader", footer="testfooter")))
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    selection_group = random.choice(old_groups)
    selection_contact = random.choice(old_contacts)
    contacts_not_in_group = database.get_contacts_not_in_group(Group(selection_group.id))
    m = 0
    for i in range(len(contacts_not_in_group)):
        if contacts_not_in_group[i].id == selection_contact.id:
            m += 1
    if m == 1:
        old_contacts_in_group = database.get_contacts_in_group(Group(selection_group.id))
        app.contact.remove_contact_from_group(selection_contact.id, selection_group.id)
        new_contacts_in_group = database.get_contacts_in_group(Group(selection_group.id))
        assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    else:
        app.contact.add_contact_in_group(selection_contact.id, selection_group.id)
        old_contacts_in_group = database.get_contacts_in_group(Group(selection_group.id))
        app.contact.remove_contact_from_group(selection_contact.id, selection_group.id)
        new_contacts_in_group = database.get_contacts_in_group(Group(selection_group.id))
        assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
