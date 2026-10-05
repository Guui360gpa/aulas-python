#Ex2. Faça um código para calcular o volume de uma esfera. O volume  v  de uma esfera
# é dado por  v=43πr3  onde  r  é o raio da esfera. (utilize variáveis)

PI = 3.14
raio = float(input("Digite o raio da esfera: "))

volume = (4/3) * PI * raio**3
print(f"O volume da esfera é igual a {volume:.2f}")