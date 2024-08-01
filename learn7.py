class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " +self.make + " is driving")

    def stop(self):
        print("This " +self.make + " is stopped")


car1 = Car("Chevy","Corvette", 2021, "blue")
car2 = Car("Ford","Mustang", 2022,"black")

print(car1.make)


car1.drive()
car1.stop()