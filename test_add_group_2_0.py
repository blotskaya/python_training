# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_untitled_test_case(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(groupname="group_name1", groupheader="group_header2", groupfooter="group_footer3"))
    app.logout()