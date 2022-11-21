# classes e instâncias
"""9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página 225). Acrescente um atributo chamado
number_served cujo valor default é 0. Crie uma instância chamada restaurant a partir dessa classe. Apresente o número
de clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o novamente. Adicione um método chamado
set_number_served() que permita definir o número de clientes atendidos. Chame esse método com um novo número e mostre
o valor novamente. Acrescente um método chamado increment_number_served() que permita incrementar o número de
clientes servidos. Chame esse método com qualquer número que você quiser e que represente quantos clientes foram
atendidos, por exemplo, em um dia de funcionamento. """


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'O restaurante {self.restaurant_name} possui culinária {self.cuisine_type}. E já serviu '
              f'{self.number_served} clientes.')

    def open_restaurant(self):
        print('O restaurante está aberto!')

    def read_number_served(self):
        print(f'Já serviu {self.number_served} clientes.')

    def set_number_served(self, valor):
        if valor >= self.number_served:
            self.number_served = valor
        else:
            print(f'Você não pode diminuir a quantidade de clientes atendidos.')

    def increment_number_served(self, incrimento):
        if incrimento < 0:
            print('Valor precisa ser positivo.')
        else:
            self.number_served += incrimento


'''restaurante = Restaurant('Halim', 'Árabe')
restaurante.describe_restaurant()
restaurante.number_served = 23

restaurante.describe_restaurant()
restaurante.set_number_served(22)
restaurante.read_number_served()
restaurante.set_number_served(24)
restaurante.read_number_served()

restaurante.increment_number_served(100)
restaurante.read_number_served()

restaurante.increment_number_served(100)
restaurante.read_number_served()'''

"""9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à sua classe User do Exercício 9.3 (
página 226). Escreva um método chamado increment_login_attempts() que incremente o valor de login_attempts em 1. 
Escreva outro método chamado reset_login_attempts() que reinicie o valor de login_attempts com 0. Crie uma instância 
da classe User e chame increment_login_attempts() várias vezes. Exiba o valor de login_attempts para garantir que ele 
foi incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). Exiba login_attempts novamente para 
garantir que seu valor foi reiniciado com 0. """


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


usuario = User('Hugo', 'Gusmão', 'hugonbgg', 'Data Engineer')

usuario.describe_user()
while usuario.login_attempts < 10:
    usuario.increment_login_attempts()
usuario.describe_user()
usuario.reset_login_attempts()
usuario.describe_user()

