import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, "
                           "email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear,"
                           "address2, phone2, notes from addressbook")
            for row in cursor:
                (id, name, middlename, surname, nickname, company, title, address, phonehome, phonemobile, phonework, phonefax,
                 mail1, mail2, mail3, hp, bday, bmonth, byear, aday, amonth, ayear, address2, phonehome2, notes) = row
                contact_list.append(Contact(id=str(id), name=name, middlename=middlename, surname=surname, nickname=nickname,
                                            company=company, title=title, address=address, phonehome=phonehome, phonemobile=phonemobile,
                                            phonework=phonework, phonefax=phonefax, mail1=mail1, mail2=mail2, mail3=mail3,
                                            hp=hp, bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth, ayear=ayear,
                                            address2=address2, phonehome2=phonehome2, notes=notes))
        finally:
            cursor.close()
        return contact_list

    def get_contact_phones_list(self):
        contact_phones_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, home, mobile, work, phone2, address, email, email2, email3 from addressbook")
            for row in cursor:
                (id, name, surname, phonehome, phonemobile, phonework, phonehome2, address, mail1, mail2, mail3) = row
                contact_phones_list.append(
                    Contact(id=str(id), name=name, surname=surname, phonehome=phonehome, phonemobile=phonemobile, phonework=phonework,
                            phonehome2=phonehome2, address=address, mail1=mail1, mail2=mail2, mail3=mail3))
        finally:
            cursor.close()
        return contact_phones_list

    def destroy(self):
        self.connection.close()