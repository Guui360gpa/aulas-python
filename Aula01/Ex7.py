# Ex7. Faça um programa para converter graus em radianos, onde  1  grau equivale a  157.3  radianos.

graus = float(input("Digite os graus: "))

radiandos = graus * (1/57.3)

print(f"{graus}º equivale a {radiandos:.2f} radiandos")