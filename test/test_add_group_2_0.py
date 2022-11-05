# -*- coding: utf-8 -*-
from model.group import Group

def test_untitled_test_case(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="group_name1", header="group_header2", footer="group_footer3"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


