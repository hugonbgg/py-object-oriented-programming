import pizza
# importando o modulo todo
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza
# importando apenas a função make_pizza do módulo pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza import make_pizza as mp
# importando a função mp do módulo make_pizza como mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
