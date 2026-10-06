def triangulo():
    for i in range(5):
        espacos = 4 - i
        simbolos = 2 * i + 1
        print(' ' * espacos + '+' * simbolos)

triangulo()