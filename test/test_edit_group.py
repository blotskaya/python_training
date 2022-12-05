from model.group import Group
import random

def test_edit_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = db.get_group_list()
    selection = random.choice(old_groups)
    group = Group(id=selection.id, name="newname", header="newheader", footer="newfooter")
    index = 0
    n = len(old_groups)
    for i in range(n):
        if old_groups[i].id == selection.id:
            index = i
        i += 1
    app.group.edit_group_by_id(selection.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)