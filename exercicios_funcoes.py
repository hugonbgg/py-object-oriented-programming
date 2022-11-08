'''8.1 – Mensagem: Escreva uma função chamada display_message() que mostre uma frase informando a todos o que você
está aprendendo neste capítulo. Chame a função e certifique-se de que a mensagem seja exibida corretamente.'''


def display_message():
    print('Learning about functions.')


display_message()

'''8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite um parâmetro title. A função deve 
exibir uma mensagem como Um dos meus livros favoritos é Alice no país das maravilhas. Chame a função e não se esqueça 
de incluir o título do livro como argumento na chamada da função. '''


def favorite_book(book_title):
    print(f'Meu livro favorito é: {book_title.title()}!')


favorite_book('A elegância do ouriço')

'''8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um tamanho e o texto de uma mensagem que deverá
ser estampada na camiseta. A função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma camiseta. Chame a função uma segunda vez usando
argumentos nomeados. '''


def make_shirt(text, size):
    print(f'A mensagem estampada na camiseta é: {text} e o tamanho da camiseta é: {size}.')


make_shirt('Goooool!', 'GG')
make_shirt(text='Vai Brasil!', size='M')

'''8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as camisetas sejam grandes
por default, com uma mensagem Eu amo Python. Crie uma camiseta grande e outra média com a mensagem default,
e uma camiseta de qualquer tamanho com uma mensagem diferente. '''


def make_shirt(text='Eu amo Python!', size='G'):
    print(f'A mensagem estampada na camiseta é: {text} e o tamanho da camiseta é: {size}.')


make_shirt()
make_shirt(size='M')
make_shirt(size='G')
make_shirt('Eu amo Javascript!', 'P')

'''8.5 – Cidades: Escreva uma função chamada
describe_city() que aceite o nome de uma cidade e seu país. A função deve exibir uma frase simples, como Reykjavik
está localizada na Islândia. Forneça um valor default ao parâmetro que representa o país. Chame sua função para três
cidades diferentes em que pelo menos uma delas não esteja no país default. '''


def describe_city(city, country='Brasil'):
    if country[-1] == 'a':
        print(f'{city} está localizada na {country}.')
    else:
        print(f'{city} está localizada no {country}.')


describe_city('São Paulo')
describe_city('Curitiba')
describe_city('Boston', 'Estados Unidos')
describe_city('Paris', 'França')
describe_city('Tokyo', 'Japão')




