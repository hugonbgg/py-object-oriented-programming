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

"""8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim:
"Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido."""


def city_country():
    city = input('Digite a cidade:')
    country = input('Digite o país:')
    print(f'{city.title()}, {country.title()}.')


city_country()

"""8.7 – Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas duas
informações. Use a função para criar três dicionários que representem álbuns
diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão
armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar o
número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor
para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
menos uma nova chamada da função incluindo o número de faixas em um álbum."""


def make_album(artist, album, faixas=''):
    artist_album = {'artista': artist, 'álbum': album}
    if faixas:
        artist_album['faixas'] = faixas
    print(artist_album)


make_album('U2', 'Live in Paris')
make_album('U2', 'Live in Paris', '12')

"""8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e o
título de um álbum. Depois que tiver essas informações, chame make_album() com
as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um
valor de saída no laço while."""


def make_album():
    coletanea = []
    while True:
        print("Pressione 'q' para sair.")
        artist = input('Digite o nome do artista:')
        if artist == 'q':
            print("'q' key pressed! Exiting...")
            break
        album = input('Digite o nome do álbum:')
        if album == 'q':
            print("'q' key pressed! Exiting...")
            break
        artist_album = {'artista': artist, 'álbum': album}
        print(artist_album)
        coletanea.append(artist_album)

    print(f'Os artistas digitados foram:{coletanea}')


make_album()
