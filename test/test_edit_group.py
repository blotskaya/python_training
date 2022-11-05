from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="newname", header="newheader", footer="newfooter"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)