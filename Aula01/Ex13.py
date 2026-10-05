# Ex13. Podemos calcular o perímetro de um círculo a partir do seu diâmetro.
# Para isso, basta obter o raio a partir do diâmetro, isto é,
# dado um diâmetro  d  obtemos o raio  r=d/2  e então aplicar a fórmula acima de perímetro.
# Reescreva nosso programa para calcular o perímetro de um círculo a partir do seu diâmetro.

PI = 3.14

d = float(input("Digite o valor do diâmetro"))

r = d/2

p = 2* PI * r**2

print(f"O perimêtro dessa circunferência é de {p:.2f}")