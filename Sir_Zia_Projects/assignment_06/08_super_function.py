#1st parent class
class Person:
    def __init__(self , name):
        self.name = name
# 2nd child class
class Teacher(Person):
    def __init__(self, name , subject):
        super().__init__(name)
        self.subject = subject
        
#3rd display
    def display(self):
        print(f"Name : {self.name}.\nSubject : {self.subject}.")
        
#4th creating object
if __name__ == "__main__":
    teacher= Teacher("Miss Anila", "English")
    teacher.display()
    