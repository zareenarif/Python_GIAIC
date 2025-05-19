from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Reactangle(Shape):
    def __init__(self , width , height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
if __name__ == "__main__":
    react=Reactangle(5,4)
    print("Areaa of Rectangle is:",react.area(),"meter square")
    