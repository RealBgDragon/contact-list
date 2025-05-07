class Contact:
    
    def __init__(self, name="", mobilePhone="", companyName="", companyOccupation="", companyAddress="", companyWebPage="",
                 phone2="", phone3="", homePhone="", officePhone="", privateEmail1="", privateEmail2="", officeEmail="",
                 address="", birthDay="", notes="", childName="", childBirthDay="", childNotes=""):

        # Personal Info
        self.name = name
        self.mobilePhone = mobilePhone
        self.phone2 = phone2
        self.phone3 = phone3
        self.homePhone = homePhone
        self.officePhone = officePhone

        # Company Info
        self.companyName = companyName
        self.companyOccupation = companyOccupation
        self.companyAddress = companyAddress
        self.companyWebPage = companyWebPage

        # Emails
        self.privateEmail1 = privateEmail1
        self.privateEmail2 = privateEmail2
        self.officeEmail = officeEmail

        # Other Info
        self.address = address
        self.birthDay = birthDay
        self.notes = notes

        # Children Info 
        self.childName = childName
        self.childBirthDay = childBirthDay
        self.childNotes = childNotes
