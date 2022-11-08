def greet_user(username):
    """Exibe uma saudação simples"""
    print(f'Hello, {username.title()}!')


greet_user('hugo')


# Argumentos posicionais
# É lido pela posição em que foram definidos na função.
def describe_pet(pet_type, pet_name):
    """Exibe informações sobre um pet"""
    print(f'''I have a {pet_type}.\nMy {pet_type}'s name is {pet_name.title()}.
    ''')


describe_pet('dog', 'Kalinda')

# Argumentos nomeados
# nome do parâmetro(variável) é passado com o seu argumento(valor) quando chamados a função.
describe_pet(pet_name='Meia-Noite', pet_type='cat')
describe_pet(pet_type='cat', pet_name='Raposa')


# valores default
# Se não for argumento um valor ele é chamado.
def describe_pet(pet_name, pet_type='Dog'):
    """Exibe informações sobre um pet"""
    print(f'''I have a {pet_type}.\nMy {pet_type}'s name is {pet_name.title()}.
    ''')


describe_pet('Kalinda')
describe_pet(pet_type='cat', pet_name='Dora')

