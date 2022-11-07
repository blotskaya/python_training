from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/edit.php")
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        #delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
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
        wd.find_element_by_css_selector("select[name=\"bday\"] > option[value=%s]" % contact.bday).click()
        wd.find_element_by_css_selector("select[name=\"bmonth\"] > option[value=%s]" % contact.bmonth).click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=%s]" % contact.aday).click()
        wd.find_element_by_css_selector("select[name=\"amonth\"] > option[value=%s]" % contact.amonth).click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.home2)
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
                self.contact_cache.append(Contact(name=name, surname=surname, id=id))
        return list(self.contact_cache)

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")