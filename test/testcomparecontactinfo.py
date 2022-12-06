import re
from model.contact import Contact

def test_info_on_homepage_with_db(app, db):
    contact_from_db = db.get_contact_phones_list()
    contact_from_home_page = app.contact.get_contact_list()
    sorted_contact_from_db = sorted(contact_from_db, key=Contact.id_or_max)
    sorted_contact_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    n = len(contact_from_home_page)
    for i in range(n):
        assert sorted_contact_from_home_page[i].name == sorted_contact_from_db[i].name
        assert sorted_contact_from_home_page[i].surname == sorted_contact_from_db[i].surname
        assert sorted_contact_from_home_page[i].address == sorted_contact_from_db[i].address
        assert sorted_contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(
            sorted_contact_from_db[i])
        assert sorted_contact_from_home_page[i].all_email_from_home_page == merge_email_like_on_home_page(sorted_contact_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phonehome, contact.phonemobile, contact.phonework, contact.phonehome2]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.mail1, contact.mail2, contact.mail3])))

