"""9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__() de Restaurant deve armazenar dois
atributos: restaurant_name e cuisine_type. Crie um método chamado describe_restaurant() que mostre essas duas
informações, e um método de nome open_restaurant() que exiba uma mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois atributos individualmente e, em seguida,
chame os dois métodos. """


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'O restaurante {self.restaurant_name} possui culinária {self.cuisine_type}.')

    def open_restaurant(self):
        print('O restaurante está aberto!')


restaurante = Restaurant('Amadeus', 'Síria')
print(restaurante.restaurant_name)
print(restaurante.cuisine_type)
restaurante.describe_restaurant()
restaurante.open_restaurant()

"""9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três instâncias diferentes da classe e chame 
describe_restaurant() para cada instância. """

restaurante_matriz = Restaurant('Baora', 'Sul-Africana')
restaurante_filial_01 = Restaurant('Amon', 'Egípcia')
restaurante_filial_02 = Restaurant('Zulu', 'da Costa do Marfim')

restaurante_matriz.describe_restaurant()
restaurante_filial_01.describe_restaurant()
restaurante_filial_02.describe_restaurant()

"""9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e, então, 
crie vários outros atributos normalmente armazenados em um perfil de usuário. Escreva um método de nome 
describe_user() que apresente um resumo das informações do usuário. Escreva outro método chamado greet_user() que 
mostre uma saudação personalizada ao usuário. Crie várias instâncias que representem diferentes usuários e chame os 
dois métodos para cada usuário. """


class User():
    def __init__(self, first_name, last_name, user_name, departament):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.departament = departament

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}, seu nome de usuário é {self.user_name} e seu departa'
              f'mento é {self.departament}.')

    def greet_user(self):
        print(f'Bem-vindo {self.user_name}!')


usuario = User('Hugo', 'Gusmão', 'hugonbgg', 'Engenharia')
print(usuario.user_name, usuario.last_name, usuario.user_name, usuario.departament)
usuario.describe_user()
usuario.greet_user()