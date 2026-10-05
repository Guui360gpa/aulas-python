# Ex10. Troque a por b sem usar nenhuma variável adicional.

a = int(input("Digite a variavel a: "))
b = int(input("Digite a variavel b: "))

a = a + b
b = a - b
a = a - b

print(f"Agora variavel a é igual a {a}")
print(f"Agora variavel b é igual a {b}")