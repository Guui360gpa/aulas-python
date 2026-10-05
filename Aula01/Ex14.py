# Ex14. O teorema de Pitágoras é um teorema muito importante que relaciona os lados
# de um triângulo retângulo. Matematicamente, o teorema é expresso pela fórmula  h2=b2+c2 ,
# onde  h  é chamado de hipotenusa e  b,c  são os catetos do triângulo.
# Escreva um programa que calcula o valor de  h .

b = float(input("Digite o primeiro cateto"))
c = float(input("Digite o segundo cateto"))

h = (b**2 + c**2) ** 0.5

print(f"O valor de hipotenusa é {h:.2f}")