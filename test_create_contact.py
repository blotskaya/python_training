# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest, time, re

class Createcontact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def create_contact(self, wd):
        #init contact creation
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/edit.php")
        #fill contact forms
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Maria")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys("Kate")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("White")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("mariakate")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("new_title")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Big Company")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Moscow, Lenina 24")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("Lenina 24")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("89991112223")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("Big Company")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("112233")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("mariakate@mail.com")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("bigcompany@mail.com")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("work@mail.com")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("mariakate.com")
        wd.find_element_by_css_selector("select[name=\"bday\"] > option[value=\"11\"]").click()
        wd.find_element_by_css_selector("select[name=\"bmonth\"] > option[value=\"December\"]").click()
        wd.find_element_by_name("byear").send_keys("1989")
        wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"7\"]").click()
        wd.find_element_by_css_selector("select[name=\"amonth\"] > option[value=\"October\"]").click()
        wd.find_element_by_name("ayear").send_keys("2020")
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Saint Petersburg")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("Lomonosova 25")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("new_notes")
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
        self.login(wd)
        self.create_contact(wd)
        self.return_to_contacts_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
