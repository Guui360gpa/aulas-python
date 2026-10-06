# Parte 1: do_twice com função e valor
def do_twice(func, valor):
    func(valor)
    func(valor)


# print_twice: imprime o valor duas vezes
def print_twice(bruce):
    print(bruce)
    print(bruce)


# Parte 2: passando print_twice e 'Spam' para do_twice
do_twice(print_twice, 'Spam')


# Parte 3: do_four com apenas duas linhas (definição + corpo)
def do_four(func, valor):
    do_twice(func, valor); do_twice(func, valor)


do_four(print_twice, 'Spam')