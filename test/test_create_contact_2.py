# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_createcontact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(name="Maria", middlename="Kate", surname="White",
                            nickname="mariakate", title="new_title", company="Big Company",
                            address="Moscow, Lenina 24", phonehome="Lenina 24", phonemobile="89991112223",
                            phonework="Big Company", phonefax="112233", mail1="mariakate@mail.com",
                            mail2="bigcompany@mail.com", mail3="work@mail.com", hp="mariakate.com",
                            byear="1989", ayear="2020", address2="Saint Petersburg",
                            home2="Lomonosova 25", notes="new_notes", bday="\"11\"",
                            bmonth="\"December\"", aday="\"7\"", amonth="\"October\""))
    app.session.logout()

