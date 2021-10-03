import datetime
class person():
    def __init__(self, name, dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today< datetime.date(today.year, self.dob.month, self.dob.day):
            age-=1
        if age>=18:
            print(self.name, " , you can vote.")
        else:
            print(self.name, " , you cannot vote.")
p=person("harsh", datetime.date(2000, 4, 2))
p.check()