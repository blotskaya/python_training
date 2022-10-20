from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(name="Jane", middlename="Lane", surname="Robert",
                               nickname="janelane", title="title", company="New Company",
                               address="Lomonosova 28", phonehome="89991112233", phonemobile="87771112233",
                               phonework="89892223311", phonefax="88984546611", mail1="janelane@mail.com",
                               mail2="newcompany@mail.com", mail3="janework@mail.com", hp="janelane.ru",
                               byear="1977", ayear="2015", address2="Moscow",
                               home2="Lenina 25", notes="otes", bday="\"9\"",
                               bmonth="\"October\"", aday="\"12\"", amonth="\"November\""))
    app.session.logout()