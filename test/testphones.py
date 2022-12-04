import re

def test_phones_on_homepage(app, db):
    contact_from_db = db.get_contact_phones_list()
    contact_from_home_page = app.contact.get_contact_list()
    n = len(contact_from_home_page)
    i = 0
    for i in range(n):
        assert contact_from_home_page[i].name == contact_from_db[i].name
        assert contact_from_home_page[i].surname == contact_from_db[i].surname
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_from_db[i])
        i += 1


#def test_phones_on_contact_view_page(app):
    #contact_from_view_page = app.contact.get_contact_from_view_page(0)
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.phonehome == contact_from_edit_page.phonehome
    #assert contact_from_view_page.phonemobile == contact_from_edit_page.phonemobile
    #assert contact_from_view_page.phonework == contact_from_edit_page.phonework
    #assert contact_from_view_page.phonehome2 == contact_from_edit_page.phonehome2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phonehome, contact.phonemobile, contact.phonework, contact.phonehome2]))))