#ex for abstraction

class Employee:
    _firstName: str = "Thulasi"
    _lastName: str = "Tendu"
    def fullName(self):
        return self._firstName+" "+self._lastName
emp = Employee()
emp._firstName = "abc"
print(emp.fullName())