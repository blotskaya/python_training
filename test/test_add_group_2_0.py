# -*- coding: utf-8 -*-
from model.group import Group

def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="group_name1", groupheader="group_header2", groupfooter="group_footer3"))
    app.session.logout()
