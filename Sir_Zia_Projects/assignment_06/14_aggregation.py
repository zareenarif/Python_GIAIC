class Employee:
    def __init__(self,name):
        self.name = name
        
class Department:
    def __init__(self, employee):
        self.employee = employee

    def show_employee(self):
        print(f"Employee in department: {self.employee.name}")
        
if __name__ == "__main__":
        emp= Employee("Zareen")
        dept = Department(emp) # type: ignore
        dept.show_employee()    
        
        del dept
        # print(dept)  error will come
        print(emp)
        