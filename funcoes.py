def greet_user(username):
    """Exibe uma saudação simples"""
    print(f'Hello, {username.title()}!')


greet_user('hugo')

'''8.1 – Mensagem: Escreva uma função chamada display_message() que mostre uma frase informando a todos o que você 
está aprendendo neste capítulo. Chame a função e certifique-se de que a mensagem seja exibida corretamente.'''


def display_message():
    print('Learning about functions.')


display_message()

'''8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite um parâmetro title. A função deve 
exibir uma 
mensagem como Um dos meus livros favoritos é Alice no país das maravilhas. Chame a função e não se esqueça de incluir 
o título do livro como argumento na chamada da função. '''


def favorite_book(book_title):
    print(f'Meu livro favorito é: {book_title.title()}!')


favorite_book('A elegância do ouriço')


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
