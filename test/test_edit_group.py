from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    app.group.edit_first_group(Group(name="newname", header="newheader", footer="newfooter"))