# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest, time, re

class Createcontact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def create_contact(self, wd, contactname, contactmiddlename, contactsurname, contactnickname, contacttitle,
                       contactcompany, contactaddress, contacthome, contactmobile, contactwork, contactfax,
                       contactmail1, contactmail2, contactmail3, contacthp, contactbyear, contactayear, contactaddress2,
                       contacthome2, contactnotes):
        #init contact creation
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/edit.php")
        #fill contact forms
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contactname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contactmiddlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contactsurname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contactnickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacttitle)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contactcompany)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contactaddress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacthome)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contactmobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contactwork)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contactfax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contactmail1)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contactmail2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contactmail3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contacthp)
        wd.find_element_by_css_selector("select[name=\"bday\"] > option[value=\"11\"]").click()
        wd.find_element_by_css_selector("select[name=\"bmonth\"] > option[value=\"December\"]").click()
        wd.find_element_by_name("byear").send_keys(contactbyear)
        wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"7\"]").click()
        wd.find_element_by_css_selector("select[name=\"amonth\"] > option[value=\"October\"]").click()
        wd.find_element_by_name("ayear").send_keys(contactayear)
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contactaddress2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contacthome2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contactnotes)
        #submit changes
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def return_to_contacts_page(self, wd):
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
    
    def test_createcontact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, contactname="Maria", contactmiddlename="Kate", contactsurname="White",
                            contactnickname="mariakate", contacttitle="new_title", contactcompany="Big Company",
                            contactaddress="Moscow, Lenina 24", contacthome="Lenina 24", contactmobile="89991112223",
                            contactwork="Big Company", contactfax="112233", contactmail1="mariakate@mail.com",
                            contactmail2="bigcompany@mail.com", contactmail3="work@mail.com", contacthp="mariakate.com",
                            contactbyear="1989", contactayear="2020", contactaddress2="Saint Petersburg",
                            contacthome2="Lomonosova 25", contactnotes="new_notes")
        self.return_to_contacts_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
