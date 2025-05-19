class Car:
    def __init__(self, brand): #public variable
        self.brand = brand
        
    def start(self): #public method
        print(f"{self.brand} is the best brand in cars....")
        
if __name__ == "__main__":
    my_car = Car("Toyota")
    print(my_car.brand)
    my_car.start()
