"""9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma
classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer versão da
classe funcionará; basta escolher aquela de que você mais gosta. Adicione um
atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva
um método para mostrar esses sabores. Crie uma instância de IceCreamStand e
chame esse método."""


class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# soverteria = IceCreamStand('Esquimó', 'Soverteria')
# soverteria.describe_restaurant()
# soverteria.open_restaurant()
# soverteria.flavors = ['vanilla', 'chocolate', 'black cherry']
# soverteria.show_flavors()

"""9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva uma classe
chamada Admin que herde da classe User escrita no Exercício 9.3 (página 226),
ou no Exercício 9.5 (página 232). Adicione um atributo privileges que armazene
uma lista de strings como "can add post", "can delete post" "can ban user",
e assim por diante. Escreva um método chamado show_privileges() que liste o
conjunto de privilégios de um administrador. Crie uma instância de Admin e chame
seu método."""


class User():
    def __init__(self, first_name, last_name, user_name, departament):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.departament = departament
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}, seu nome de usuário é {self.user_name} e seu departa'
              f'mento é {self.departament}. Atualmente foram feitas {self.login_attempts} tentativas de login.')

    def greet_user(self):
        print(f'Bem-vindo {self.user_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Tentivas de login resetadas!")


class Admin(User):
    def __init__(self, first_name, last_name, user_name, departament):
        super().__init__(first_name, last_name, user_name, departament)
        self.privileges = []

    def show_privileges(self):
        print(f'Os privilégios do usuário são:')
        for privilege in self.privileges:
            print(f'{privilege}.')


# usuario = User('Hugo', 'Gusmão', 'hugonbgg', 'Data Engineer')
# usuario.describe_user()
# usuario.greet_user()

# administrador = Admin('Hugo', 'Gusmão', 'hugonbgg', 'Data Engineer')
# administrador.describe_user()
# administrador.greet_user()
# administrador.privileges = ['Criar Usuários', 'Deletar Usuários', 'Remover Permissões']
# administrador.show_privileges()

"""9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie uma
instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios."""


class User:
    def __init__(self, first_name, last_name, user_name, departament):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.departament = departament
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}, seu nome de usuário é {self.user_name} e seu departa'
              f'mento é {self.departament}. Atualmente foram feitas {self.login_attempts} tentativas de login.')

    def greet_user(self):
        print(f'Bem-vindo {self.user_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Tentivas de login resetadas!")


class Privileges:
    def __init__(self):
        self.privileges_list = []

    def show_privileges(self):
        print(f'Os privilégios do usuário são:')
        for privilege in self.privileges_list:
            print(f'{privilege}.')


class Admin(User):
    def __init__(self, first_name, last_name, user_name, departament):
        super().__init__(first_name, last_name, user_name, departament)
        self.privileges = Privileges()


# administrador = Admin('Hugo', 'Gusmão', 'hugonbgg', 'Data Engineer')
# administrador.describe_user()
# administrador.greet_user()
# administrador.privileges.privileges_list = ['Criar Usuários', 'Deletar Usuários', 'Remover Permissões']
# administrador.privileges.show_privileges()

"""9.9 – Upgrade de bateria: Use a última versão de electric_car.py desta seção.
Acrescente um método chamado upgrade_battery() na classe Battery. Esse
método deve verificar a capacidade da bateria e defini-la com 85 se o valor for
diferente. Crie um carro elétrico com uma capacidade de bateria default, chame
get_range() uma vez e, em seguida, chame get_range() uma segunda vez após
fazer um upgrade da bateria. Você deverá ver um aumento na distância que o
carro é capaz de percorrer."""


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

carro = Car('Honda', 'Civic', 2022)
print(carro.get_descriptive_name())
carro.read_odometer()
carro.increment_odometer(100)
carro.read_odometer()


print("Make an electric car, and check the range:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.get_range()

print("\nUpgrade the battery, and check the range again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 75
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()