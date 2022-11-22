class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, filled):
        self.gas_tank = filled

    def read_gas_tank(self):
        print(f"This car has {self.gas_tank} liters of gas.")


carro = Car('Honda', 'Acura', 2019)
carro.get_descriptive_name()
carro.read_odometer()
carro.update_odometer(23)
carro.read_odometer()
carro.increment_odometer(100)
carro.read_odometer()
carro.read_gas_tank()
carro.fill_gas_tank(50)
carro.read_gas_tank()


class EletricCar(Car):
    """Presenta aspectos especificos de veiculos elétricos"""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print(f"This car has a {self.battery_size} kwh battery.")

    def read_gas_tank(self):
        print("This car doesn't need a gas tank!")

    def fill_gas_tank(self):
        """Veiculos elétricos não tem tanques de gasolina"""
        print("This car doesn't need a gas tank!")


carro_eletrico = EletricCar('Tesla', 'Model S', 2019)
print(carro_eletrico.get_descriptive_name())
carro_eletrico.describe_battery()
carro_eletrico.battery_size = 100
carro_eletrico.describe_battery()
carro_eletrico.fill_gas_tank()
carro_eletrico.read_gas_tank()

