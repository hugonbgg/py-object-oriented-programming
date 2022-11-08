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


# Valores de retorno (return)

def formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = f'{first_name} {last_name}'
    return full_name.title()


nome = formatted_name('hugo', 'gusmão')
print(nome)

musician = formatted_name('jimi', 'hendrix')
print(musician)


# Deixando um argumento opcional - nome do meio


def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
        return full_name.title()
    else:
        full_name = f'{first_name} {last_name}'
        return full_name.title()


nome_simples = formatted_name('jimi', 'hendrix')
nome_composto = formatted_name('john', 'hooker', 'lee')

print(nome_simples)
print(nome_composto)


# Devolvendo um dicionário
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


pessoa_dict = build_person('Hugo', 'Gusmão')
print(pessoa_dict)

pessoa_dict = build_person('Hugo', 'Gusmão', 36)
print(pessoa_dict)


# Usando uma função com um laço while
# Salvando várias pessoas

def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name


# Este é um loop infinito
while True:
    print('\nPlease tell me your name:')
    print("\nPress 'q' at any time to quit")
    f_name = input('First name: ')
    if f_name == 'q':
        print("'q' key pressed! Exiting...")
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        print("'q' key pressed! Exiting...")
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}!')


