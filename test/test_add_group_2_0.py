# -*- coding: utf-8 -*-
from model.group import Group

def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group_name1", header="group_header2", footer="group_footer3"))
    app.session.logout()
