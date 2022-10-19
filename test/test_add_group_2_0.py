# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="group_name1", groupheader="group_header2", groupfooter="group_footer3"))
    app.session.logout()
