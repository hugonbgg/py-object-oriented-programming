class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f'{self.make} {self.model} {self.year}'
        return long_name.title()


class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f'This car has a {self.battery_size} kWh battery.')

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approximately {range} miles on a full charge.'
        print(message)


class EletricCar(Car):
    "Representa aspectos especificos de veículos elétricos."

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai. Em seguida, inicializa os atributos especificos de um carro
        eletrico."""
        super().__init__(make, model, year)
        self.battery = Battery()


carro = Car('Honda', 'Civic', 2022)
carro_eletrico = EletricCar('Tesla', 'Model S', 2023)

print(carro.get_descriptive_name())

print(carro_eletrico.get_descriptive_name())
carro_eletrico.battery.describe_battery()
carro_eletrico.battery.get_range()


