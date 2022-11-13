from sys import maxsize

class Contact:
    def __init__(self, name=None, middlename=None, surname=None, nickname=None, title=None, company=None,
                 address=None, phonehome=None, phonemobile=None, phonework=None, phonefax=None, mail1=None, mail2=None,
                 mail3=None, hp=None, byear=None, ayear=None, address2=None, phonehome2=None, notes=None,
                 bday=None, bmonth=None, aday=None, amonth=None, id=None, all_phones_from_home_page=None,
                 all_email_from_home_page=None):
        self.name = name
        self.middlename = middlename
        self.surname = surname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phonehome = phonehome
        self.phonemobile = phonemobile
        self.phonework = phonework
        self.phonefax = phonefax
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.hp = hp
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phonehome2 = phonehome2
        self.notes = notes
        self.bday = bday
        self.aday = aday
        self.bmonth = bmonth
        self.amonth = amonth
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.surname == other.surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

