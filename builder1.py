class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Carro con motor: {self.engine}, ruedas: {self.wheels}, color: {self.color}"
    

class CarBuilder:
    def __init__(self):
        self.car = Car()
    
    def build_engine(self, engine):
        self.car.engine = engine
        return self
    
    def build_wheels(self, wheels):
        self.car.wheels = wheels
        return self
    
    def build_color(self, color):
        self.car.color = color
        return self
    
    def get_car(self):
        return self.car

builder = CarBuilder()
car = builder.build_engine("V8").build_wheels("4").build_color("Rojo").car

print(car)