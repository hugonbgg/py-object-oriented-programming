# modificando uma lista em uma função
# Começa com alguns designs que devem ser impressos

"""
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complete_models = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere cada design para completed_models após a impressão
while len(unprinted_designs) > 0:
    current_design = unprinted_designs.pop()

# Simula a criação de uma impressão 3D a partir do design
    print(f'Printing model: {current_design}')
    complete_models.append(current_design)

# Exibe todos os modelos finalizados
print(f'The following models have been printed:')
for complete_model in complete_models:
    print(complete_model)

"""


# Reescrevendo o código em funções

def print_models(unprinted_designs, completed_models):
    # Simula a impressão de cada design, até que não haja mais nenhum
    # Transfere cada design para completed_models após a impressão
    while len(unprinted_designs) > 0:
        current_design = unprinted_designs.pop()

        # Simula a criação de uma impressão 3D a partir do design
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # Exibe todos os modelos finalizados
    print(f'The following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs_list = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models_list = []

# print_models(unprinted_designs_list, completed_models_list)
# show_completed_models(completed_models_list)


# Evitando que uma função modifique uma lista
# Utiliza o ':' ao passar a lista "nome_da_função(nome_da_lista[:])"

print_models(unprinted_designs_list[:], completed_models_list)
show_completed_models(completed_models_list)
print(unprinted_designs_list)
