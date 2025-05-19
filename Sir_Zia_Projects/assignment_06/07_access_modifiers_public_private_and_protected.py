class Employee:
    def __init__(self ,name ,salary ,ssn):
        self.name = name       #public variable
        self._salary = salary  #protected varialb
        self.__ssn = ssn       #private variable
if __name__ == "__main__":
    emp = Employee("Zareen", 0 ,"123-45-6789")
    #access public variable
    print("Public Variable:", emp.name)
    #access protected variable
    print("Protected Variable:", emp._salary)
    #access private variable 
    
    try :
      print("Private Variable:", emp.__ssn)
      
    except AttributeError:
        print("Cannot access private Variable __ssn")  