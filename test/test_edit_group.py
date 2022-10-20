from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="newname", header="newheader", footer="newfooter"))
    app.session.logout()