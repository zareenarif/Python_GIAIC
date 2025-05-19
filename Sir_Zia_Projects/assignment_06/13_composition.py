class Engine:
    def Start(self):
        print("Engine is startig.")
        
class Car:
    def __init__(self):
        self.engine = Engine() #composition
        
    def start_car(self):
        self.engine.Start()
        
if __name__ == "__main__":
    my_car = Car()
    my_car.start_car()
    