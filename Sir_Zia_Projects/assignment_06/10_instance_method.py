class Dog:
    def __init__(self,name,breed):
        self.name = name  # instance variable
        self.breed = breed
        
    def bark(self):# instance method
        print(f"{self.name} is barking!")
        
if __name__ == "__main__":
    # creating an object(instance)
    my_dog = Dog("Tommy" , "Labrador")
    # call the method
    my_dog.bark()