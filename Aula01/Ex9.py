# Ex9. Escreva um programa para fazer um swap entre duas variáveis inteiras
# (swap é uma operação que troca o valor em memória de uma variável pelo da outra).

a = input("Digite a variavel a: ")
b = input("Digite a variavel b: ")

aux = a
a = b
b = aux

print(f"Agora variavel a é igual a {a}")
print(f"Agora variavel b é igual a {b}")