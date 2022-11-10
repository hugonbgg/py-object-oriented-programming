# Fundamentos sobre classes
class Dog():
    "Uma tentativa de modelar um cachorro"

    def __init__(self, name, age):
        """Inicializa os atributos name a age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando em resposta a um commando."""
        print(f'{self.name.title()} is now sitting!')

    def roll_over(self):
        """Simula um cachorro sentando em resposta a um commando."""
        print(f'{self.name.title()} rolled over!')

my_dog = Dog('Kalinda', 6)
print(my_dog)
print(my_dog.name)
print(my_dog.age)


print(f"My dog's name is {my_dog.name.title()}, she is {my_dog.age} years old.")

my_dog.roll_over()
my_dog.sit()

