class Student:
    def __init__(self, sid, name, dept, year, email, phone, status="ACTIVE"):
        self.id = sid
        self.name = name
        self.dept = dept
        self.year = year
        self.email = email
        self.phone = phone
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "dept": self.dept,
            "year": self.year,
            "email": self.email,
            "phone": self.phone,
            "status": self.status
        }