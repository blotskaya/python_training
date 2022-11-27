from model.contact import Contact

import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_css_selector('input[type="submit"]').click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element_by_css_selector('img[alt="Edit"]').click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def select_contact_by_index_for_del(self, index):
        wd = self.app.wd
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index_for_del(index)
        #delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        #delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        self.fill_contact_form(contact)
        #submit
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        self.fill_contact_form(contact)
        #submit
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        # open contacts page
        if not wd.current_url.endswith("/index.php"):
            wd.get("http://localhost/addressbook/index.php")

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact forms
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phonehome)
        self.change_field_value("mobile", contact.phonemobile)
        self.change_field_value("work", contact.phonework)
        self.change_field_value("fax", contact.phonefax)
        self.change_field_value("email", contact.mail1)
        self.change_field_value("email2", contact.mail2)
        self.change_field_value("email3", contact.mail3)
        self.change_field_value("homepage", contact.hp)
        wd.find_element_by_css_selector('select[name="bday"] > option[value=%s]' % contact.bday).click()
        wd.find_element_by_css_selector('select[name="bmonth"] > option[value=%s]' % contact.bmonth).click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_css_selector('select[name="aday"] > option[value=%s]' % contact.aday).click()
        wd.find_element_by_css_selector('select[name="amonth"] > option[value=%s]' % contact.amonth).click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phonehome2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[2].text
                surname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                allphones = cells[5].text
                allmails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(name=name, surname=surname, id=id,
                                                  all_phones_from_home_page=allphones,
                                                  all_email_from_home_page=allmails, address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        surname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phonehome = wd.find_element_by_name("home").get_attribute("value")
        phonemobile = wd.find_element_by_name("mobile").get_attribute("value")
        phonework = wd.find_element_by_name("work").get_attribute("value")
        phonehome2 = wd.find_element_by_name("phone2").get_attribute("value")
        mail1 = wd.find_element_by_name("email").get_attribute("value")
        mail2 = wd.find_element_by_name("email2").get_attribute("value")
        mail3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(name=name, surname=surname, id=id, phonehome=phonehome,
                        phonemobile=phonemobile, phonework=phonework, phonehome2=phonehome2,
                        mail1=mail1, mail2=mail2, mail3=mail3, address=address)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        phonehome = re.search("H: (.*)", text).group(1)
        phonework = re.search("W: (.*)", text).group(1)
        phonemobile = re.search("M: (.*)", text).group(1)
        phonehome2 = re.search("P: (.*)", text).group(1)
        return Contact(phonehome=phonehome,phonemobile=phonemobile, phonework=phonework, phonehome2=phonehome2)

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")