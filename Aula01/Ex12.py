# Ex12. Escreva um programa que calcula o perímetro (circunferência)
# de um círculo  p=2πr2  onde  r  é o raio do círculo.

PI = 3.14

r = float(input("Digite o valor do raio: "))

p = 2* PI * r**2

print(f"O perimêtro dessa circunferência é de {p:.2f}")